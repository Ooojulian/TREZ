# 📋 Guión de Sustentación - TREZ Language

## 🎯 ESTRUCTURA DE LA PRESENTACIÓN (15-20 minutos)

---

## I. INTRODUCCIÓN (2 min)

**"TREZ es un lenguaje de programación de dominio específico (DSL) enfocado en Deep Learning, desarrollado completamente desde cero sin dependencias externas"**

### Puntos clave a mencionar:
- ✅ DSL (Domain Specific Language)
- ✅ Enfocado en Deep Learning
- ✅ Sin NumPy, PyTorch, ni dependencias externas
- ✅ Implementado con paradigma funcional
- ✅ Usa patrón Visitor para interpretar código

---

## II. ARQUITECTURA TÉCNICA (5 min)

### A. El flujo principal

```
Código TREZ (.trez)
    ↓
ANTLR4 Lexer/Parser (genera AST)
    ↓
TrezVisitor (Patrón Visitor) ← EL CEREBRO
    ↓
Evaluación funcional
    ↓
Resultado
```

**Puedes mostrar este diagrama en una diapositiva**

### B. El "cerebro": visitor.py

**Responde:** "El cerebro está en `src/visitor.py`, clase `TrezVisitor` (líneas 11-227)"

```python
class TrezVisitor(AntlrTrezVisitor):  # Línea 11
    def visitProgram(self, ctx): ...
    def visitLet_stmt(self, ctx): ...
    def visitAddSubExpr(self, ctx): ...
    def visitFuncCallExpr(self, ctx): ...
    # ... un método para CADA tipo de nodo
```

**Nota:** Cada nodo del AST tiene un método `visit[Tipo]()` que lo procesa.

### C. Ejemplo en vivo: `5 + 3 * 2`

```
Código TREZ:
  5 + 3 * 2;

AST (respeta precedencia):
        AddSub
        /     \
      NUM(5)  MulDiv
              /     \
            NUM(3)  NUM(2)

Ejecución del Visitor:
  visitAddSubExpr()
    left = visit(NUM(5)) = 5
    right = visit(MulDiv)
            → visitMulDivExpr() = 3 * 2 = 6
    → 5 + 6 = 11

Salida: 11
```

---

## III. PARADIGMA FUNCIONAL (3 min)

### A. ¿Dónde está la "pureza funcional"?

**Responde:** "En cada método del visitor se aplica el paradigma funcional"

**Ejemplo 1: Suma (pura)**
```python
def visitAddSubExpr(self, ctx):
    left = self.visit(ctx.expr(0))    # Evalúa sin modificar
    right = self.visit(ctx.expr(1))   # Evalúa sin modificar
    # NO modifica left, right, ni ningún estado
    return left + right               # ← PURA: entrada → salida
```

**Ejemplo 2: Variables (bindings funcionales)**
```python
def visitLet_stmt(self, ctx):
    var_name = ctx.ID().getText()
    value = self.visit(ctx.expr())
    self.memory[var_name] = value     # ← BINDING: x ↦ 10
    return value
```

**Ejemplo 3: Sin efectos secundarios**
```python
# NO hacemos esto (IMPURO):
def visitAddSubExpr_impuro(self, ctx):
    self.global_count += 1            # ¡EFECTO SECUNDARIO!
    print(f"Sumando...")               # ¡EFECTO SECUNDARIO!
    return left + right

# Hacemos esto (PURO):
def visitAddSubExpr_puro(self, ctx):
    # Solo calcula y devuelve
    return left + right
```

### B. ¿Cómo se almacenan variables sin mutación?

**Responde:** "Usamos un diccionario `self.memory` como 'bindings' funcionales"

```python
class TrezVisitor(AntlrTrezVisitor):
    def __init__(self):
        self.memory = {}  # ← Mapeo de variables a valores
```

**Código TREZ:**
```
let x = 5;
let y = x + 3;
y;
```

**Estado del memory:**
```
memory = {}
memory = {"x": 5}
memory = {"x": 5, "y": 8}
→ Imprime: 8
```

---

## IV. PATRÓN VISITOR (3 min)

### A. ¿Qué es el patrón Visitor?

**Responde:** "Es un patrón de diseño que separa la estructura (AST) de la operación (visitación)"

### B. Cómo funciona en TREZ

```
Cada nodo → Un método visit[Tipo]()

Ejemplo:
- NumExprContext → visitNumExpr()
- AddSubExprContext → visitAddSubExpr()
- VarExprContext → visitVarExpr()
- FuncCallExprContext → visitFuncCallExpr()
- ...
```

### C. Despacho automático de ANTLR

**ANTLR automáticamente hace:**
```python
def visit(self, node):
    method_name = f"visit{node.__class__.__name__}"
    method = getattr(self, method_name)
    return method(node)
```

### D. Flujo visual completo

```
            Program (visitProgram)
              |
         Expr_stmt (visitExpr_stmt)
              |
           AddSub (visitAddSubExpr)
          /      \
        Num      MulDiv (visitMulDivExpr)
        (5)      /      \
              Num        Num
              (3)        (2)

Ejecución: Recorre el árbol recursivamente
de abajo hacia arriba (post-order)
```

---

## V. FUNCIONES MATEMÁTICAS NATIVAS (2 min)

### A. ¿Por qué sin dependencias externas?

**Responde:** "Implementamos todas las funciones matemáticas usando series de Taylor/Maclaurin"

### B. Ejemplos de implementación nativa

**Ubicación:** `src/lib/math/core.py`

```python
def exp(x, terms=30):
    """e^x usando Serie de Maclaurin"""
    # e^x = 1 + x + x²/2! + x³/3! + ...
    result = 1.0
    term = 1.0
    for i in range(1, terms):
        term *= (x / i)
        result += term
    return result

def sin(x, terms=20):
    """sin(x) usando Serie de Taylor"""
    # Reduce rango: x = x % (2*PI)
    # sin(x) = x - x³/3! + x⁵/5! - ...
    result = 0.0
    sign = 1
    for n in range(terms):
        term = pow(x, 2*n + 1) / factorial(2*n + 1)
        result += sign * term
        sign *= -1
    return result
```

### C. Funciones disponibles

| Función | Tipo | Ubicación |
|---------|------|-----------|
| `abs()`, `pow()`, `sqrt()` | Algebraica | core.py |
| `exp()`, `log()` | Trascendental | core.py |
| `sin()`, `cos()`, `tan()` | Trigonometría | core.py |
| `relu()`, `sigmoid()` | Activación | activations.py |
| `mse()`, `mse_grad()` | Pérdida | losses.py |
| `dot()`, `transpose()` | Tensor | tensor.py |

---

## VI. CONTROL DE PRECISIÓN DE DECIMALES (2 min)

**Pregunta esperada:** "¿Cómo controlas los decimales cuando divides?"

### A. Respuesta técnica

**Ubicación:** `src/visitor.py` líneas 27-30

```python
def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    print(result)  # ← AQUÍ SE CONTROLA LA SALIDA
    return result
```

### B. Cómo cambiar la precisión

**Opción 1: Redondeo simple**
```python
def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    if isinstance(result, float):
        print(round(result, 4))  # ← Máximo 4 decimales
    else:
        print(result)
    return result
```

**Opción 2: Mostrar enteros sin decimales**
```python
def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    if isinstance(result, float) and result == int(result):
        print(int(result))  # 5.0 → 5
    elif isinstance(result, float):
        print(round(result, 4))
    else:
        print(result)
    return result
```

### C. Ejemplo en vivo

```
Código TREZ:
  10 / 3;

Salida actual:
  3.3333333333333335

Con round(result, 4):
  3.3333

Con round(result, 2):
  3.33
```

---

## VII. FLUJO DE UNA FUNCIÓN MATH (2 min)

**Pregunta esperada:** "¿Cómo se calcula sin(PI/2)?"

### A. Respuesta paso a paso

**Código TREZ:**
```
sin(PI / 2);
```

**Ejecución:**

```
visitFuncCallExpr()
  func_name = "sin"
  args = [visit(DIVIDE PI / 2)]
  
  Evalúa PI / 2:
    visit(VarExpr "PI")
      → math_utils.constants["PI"]
      → 3.14159265...
    
    visit(NumExpr "2")
      → 2
    
    PI / 2 = 1.57079632...
  
  args = [1.57079632...]
  
  func_name == "sin" → True
  return math_utils.sin(1.57079632...)
    → Calcula con serie de Taylor en math/core.py
    → 1.0
```

---

## VIII. MEJORAS REALIZADAS EN ESTA ENTREGA (2 min)

### A. Limpieza de código

- ✅ Removí sufijos "doz" (nomenclatura profesional)
- ✅ Reorganicé librerías: `mathdoz/` → `math/`, etc.
- ✅ Actualizé todas las importaciones

### B. Ejemplos comprensivos

- ✅ 8 ejemplos progresivos en `/examples`
- ✅ Desde operaciones básicas hasta I/O

### C. Tests exhaustivos

- ✅ 60+ tests en `/tests`
- ✅ `test_math_core.py`: Funciones matemáticas
- ✅ `test_tensor_operations.py`: Álgebra lineal
- ✅ `test_activations.py`: Activaciones
- ✅ `test_losses.py`: Pérdidas

### D. Documentación

- ✅ README.md mejorado con ejemplos
- ✅ Design.md actualizado con fase actual
- ✅ RESPUESTAS_PROFESOR.md: Guía técnica
- ✅ EJEMPLOS_PRACTICOS.md: Código en vivo

---

## IX. RESPUESTAS A PREGUNTAS COMUNES

### P: "¿Dónde está el cerebro del proyecto?"
**R:** En `src/visitor.py`, clase `TrezVisitor` (líneas 11-227)

### P: "¿Cómo manejas la recursión?"
**R:** Cada `visit()` llama a otros `visit()` recursivamente. Ejemplo: `visitAddSubExpr` llama a `visit(expr(0))` y `visit(expr(1))`

### P: "¿Dónde controlo la precisión de decimales?"
**R:** En `visitExpr_stmt` (línea 29), puedo agregar `round(result, N)`

### P: "¿Dónde se guardan las variables?"
**R:** En `self.memory` dict (línea 14). `visitLet_stmt` las guarda, `visitVarExpr` las recupera.

### P: "¿Por qué usas el patrón Visitor y no otro?"
**R:** Porque separa la estructura (AST) de la lógica (visitación). Es extensible y fácil de entender.

### P: "¿Dónde está el paradigma funcional?"
**R:** En métodos puros sin efectos secundarios. Cada `visit()` evalúa y devuelve sin modificar estado.

### P: "¿Cómo se llaman funciones como `sin()` o `relu()`?"
**R:** En `visitFuncCallExpr` (línea 42-89), hago dispatch: si `func_name == 'sin'`, llamo `math_utils.sin(args[0])`

### P: "¿Qué pasa cuando hay un error de sintaxis?"
**R:** En `main.py` líneas 24-28, uso `TrezErrorListener` para capturar errores de ANTLR4

### P: "¿Soportas recursión o funciones definidas por usuario?"
**R:** Aún no, es parte de Fase 3. Hoy solo funciones built-in.

---

## X. DEMOSTRACIÓN EN VIVO (3 min)

### Demo 1: Operación simple
```bash
python src/main.py examples/01_basic_math.trez
```

**Esperado:**
```
11      # (5 + 3) * 2 / 4 = 4, pero hay otras operaciones
4       # 10 - 2 * 3 = 4
```

### Demo 2: Variables y funciones
```bash
python src/main.py examples/02_variables.trez
```

**Esperado:**
```
15      # PI * 5 * 5
78.5    # (aproximadamente)
```

### Demo 3: Activaciones
```bash
python src/main.py examples/04_activation_functions.trez
```

**Esperado:**
```
5
0
[1, 0, 3, 0]   # relu([1, -2, 3, -4])
0.5             # sigmoid(0)
```

### Demo 4: Funciones de pérdida
```bash
python src/main.py examples/05_loss_functions.trez
```

**Esperado:**
```
0.02    # mse([0, 1, 0], [0.1, 0.9, 0.2])
```

---

## XI. CONCLUSIÓN Y PRÓXIMOS PASOS (1 min)

### Logros
- ✅ Intérprete funcional sin dependencias externas
- ✅ 60+ funciones matemáticas nativas
- ✅ Patrón Visitor bien implementado
- ✅ Paradigma funcional en acción

### Próximos pasos (Fase 3-4)
- 🚧 Autograd (diferenciación automática)
- 🔮 Entrenamiento de redes neuronales
- 🔮 Redes Siamesas y Autoencoders

---

## 📝 TARJETAS DE REFERENCIA RÁPIDA

### Localizar código rápidamente

| Pregunta | Respuesta |
|----------|-----------|
| Dónde sumar | `visitor.py:207-208` visitAddSubExpr |
| Dónde multiplicar | `visitor.py:131-132` visitMulDivExpr |
| Dónde variables | `visitor.py:24` visitLet_stmt |
| Dónde funciones | `visitor.py:42-89` visitFuncCallExpr |
| Dónde imprimir | `visitor.py:29` visitExpr_stmt |
| Dónde exp() | `math/core.py:61` def exp |
| Dónde sin() | `math/core.py:104` def sin |
| Dónde relu() | `activations.py:13` def relu |
| Dónde mse() | `losses.py:3` def mse |

---

**¡LISTO PARA LA SUSTENTACIÓN! 🚀**
