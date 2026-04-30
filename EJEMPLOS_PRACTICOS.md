# 🔧 Ejemplos Prácticos: Modificando el Código del Visitor

## ESCENARIO 1: Profesor pregunta "¿Cómo cambias la precisión de decimales?"

### Paso 1: Ver el problema actual

**Archivo TREZ:** `test_decimals.trez`
```trez
10 / 3;
15 / 7;
1 / 3;
```

**Salida actual:**
```
3.3333333333333335
2.142857142857143
0.3333333333333333
```

### Paso 2: Localizar dónde se imprime

**Archivo:** `src/visitor.py` líneas 27-30

```python
def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    print(result)  # ← AQUÍ SE IMPRIME
    return result
```

### Paso 3: Hacer el cambio

```python
def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    
    # Solución: Controlar decimales
    if isinstance(result, float):
        # Muestra máximo 4 decimales
        formatted = round(result, 4)
        print(formatted)
    else:
        print(result)
    
    return result
```

### Resultado:
```
3.3333
2.1429
0.3333
```

---

## ESCENARIO 2: Profesor pregunta "¿Cómo tratas números enteros vs flotantes?"

### El código hoy:

```python
def visitNumExpr(self, ctx: TrezParser.NumExprContext):  # Línea 212
    val = ctx.getText()  # texto: "5" o "3.14"
    return float(val) if '.' in val else int(val)
```

### Demostración:

```trez
5;          // int → 5
5.0;        // float → 5.0
5 + 1;      // int + int → 6
5.0 + 1;    // float + int → 6.0
```

### Problema: `5.0` se ve feo como `5.0` si debería ser `5`

**Solución mejorada:**

```python
def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    
    # Si un float es realmente un entero, muéstralo sin decimales
    if isinstance(result, float) and result == int(result):
        print(int(result))
    elif isinstance(result, float):
        print(round(result, 4))
    else:
        print(result)
    
    return result
```

**Ahora:**
```
5           ← Se ve como entero (aunque Python lo calcule como 5.0)
5.0         ← Entrado como flotante, se ve como 5
3.3333      ← Realmente flotante, se redondea
```

---

## ESCENARIO 3: Profesor pregunta "¿Dónde está la lógica de sumar?"

### Respuesta con código:

**Archivo:** `src/visitor.py` líneas 193-210

```python
def visitAddSubExpr(self, ctx: TrezParser.AddSubExprContext):
    # Paso 1: Evalúa la expresión izquierda
    left = self.visit(ctx.expr(0))
    
    # Paso 2: Evalúa la expresión derecha
    right = self.visit(ctx.expr(1))
    
    # Paso 3: Obtiene el operador (+, -)
    op = ctx.getChild(1).getText()
    
    # Paso 4: Aplica la operación
    if op == '+':
        return left + right
    else:
        return left - right
```

### Ejemplo: `5 + 3 * 2`

```
visitAddSubExpr()
  left = visit(expr(0))
         → visit(NumExpr "5")
         → visitNumExpr()
         → return 5
  
  right = visit(expr(1))
          → visit(MulDivExpr "3 * 2")
          → visitMulDivExpr()
            → left = visit(NumExpr "3") = 3
            → right = visit(NumExpr "2") = 2
            → op = "*"
            → return 3 * 2 = 6
  
  op = "+"
  return 5 + 6 = 11
```

---

## ESCENARIO 4: Profesor pregunta "¿Cómo funcionan las variables?"

### El código:

**Guardar variable:** línea 21-25
```python
def visitLet_stmt(self, ctx: TrezParser.Let_stmtContext):
    var_name = ctx.ID().getText()      # "x"
    value = self.visit(ctx.expr())     # evalúa 5 + 3 = 8
    self.memory[var_name] = value      # memory["x"] = 8
    return value
```

**Recuperar variable:** línea 32-40
```python
def visitVarExpr(self, ctx: TrezParser.VarExprContext):
    var_name = ctx.ID().getText()      # "x"
    
    # Busca en constantes primero
    if hasattr(math_utils, 'constants') and var_name in math_utils.constants:
        return math_utils.constants[var_name]
    
    # Luego busca en memoria
    if var_name in self.memory:
        return self.memory[var_name]    # memory["x"] = 8
    
    raise TrezRuntimeError(f"Undefined variable: '{var_name}'")
```

### Flujo completo:

```trez
let x = 5 + 3;
let y = x * 2;
y;
```

**Ejecución:**
```
memory = {}

Línea 1: visitLet_stmt()
  var_name = "x"
  value = visit(AddSub 5 + 3)
        = 8
  memory["x"] = 8
  memory = {"x": 8}

Línea 2: visitLet_stmt()
  var_name = "y"
  value = visit(MulDiv x * 2)
        = visit(VarExpr "x") * visit(NumExpr "2")
        = memory["x"] * 2
        = 8 * 2
        = 16
  memory["y"] = 16
  memory = {"x": 8, "y": 16}

Línea 3: visitExpr_stmt()
  result = visit(VarExpr "y")
         = memory["y"]
         = 16
  print(16)
  return 16
```

---

## ESCENARIO 5: Profesor pregunta "¿Dónde se llaman funciones como sin(), cos()?"

### El código: línea 42-89

```python
def visitFuncCallExpr(self, ctx: TrezParser.FuncCallExprContext):
    func_name = ctx.ID().getText()  # "sin", "cos", "relu", etc.
    args = [self.visit(expr_ctx) for expr_ctx in ctx.expr()]  # Evalúa argumentos
    
    # DISPATCH: selecciona qué función ejecutar
    if func_name == 'sin':
        return math_utils.sin(args[0])
    elif func_name == 'cos':
        return math_utils.cos(args[0])
    elif func_name == 'exp':
        return math_utils.exp(args[0])
    # ... más funciones
```

### Ejemplo: `sin(PI / 2)`

```
visitFuncCallExpr()
  func_name = "sin"
  
  args = [visit(DIVIDE PI / 2)]
       = [visit(VarExpr "PI") / visit(NumExpr "2")]
  
  visit(VarExpr "PI")
    → math_utils.constants["PI"]
    → 3.14159265358979323846
  
  visit(NumExpr "2")
    → 2
  
  args = [3.14159265358979323846 / 2]
       = [1.57079632679489661923]
  
  func_name == 'sin' → True
  return math_utils.sin(1.57079632679489661923)
         → (calcula con serie de Taylor en math/core.py)
         → 1.0
```

---

## ESCENARIO 6: Profesor pregunta "¿Dónde está el paradigma funcional?"

### Respuesta directa:

**Punto 1:** Variables como "bindings" (línea 14)
```python
self.memory = {}  # No modifica, solo vincula
```

**Punto 2:** Sin efectos secundarios (línea 193-210)
```python
def visitAddSubExpr(self, ctx):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))
    # NO modifica left, right, ni ningún estado
    return left + right  # ← Puro: (entrada) → (salida)
```

**Punto 3:** Recursión (línea 94-95)
```python
def visitBlock(self, ctx):
    result = None
    for stmt in ctx.statement():
        result = self.visit(stmt)  # ← Visita recursivamente
    return result
```

### Contraste: Código impuro vs puro

```python
# IMPURO (con efectos secundarios):
def visitAddSubExpr_impuro(self, ctx):
    self.global_operations += 1  # ¡EFECTO SECUNDARIO!
    self.cache[id(ctx)] = left + right  # ¡EFECTO SECUNDARIO!
    print(f"Sumando: {left} + {right}")  # ¡EFECTO SECUNDARIO!
    return left + right

# PURO (sin efectos secundarios):
def visitAddSubExpr_puro(self, ctx):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))
    return left + right  # Solo devuelve, sin modificar nada
```

---

## ESCENARIO 7: Profesor pregunta "¿Dónde está el patrón Visitor?"

### La esencia del Visitor (línea 11):

```python
class TrezVisitor(AntlrTrezVisitor):  # Hereda de Visitor base
    def visitProgram(self, ctx): ...
    def visitExpr_stmt(self, ctx): ...
    def visitAddSubExpr(self, ctx): ...
    def visitNumExpr(self, ctx): ...
    # ... un método para cada tipo de nodo
```

### Cómo ANTLR automáticamente despacha:

```python
# main.py línea 40:
visitor.visit(tree)

# Internamente ANTLR hace (pseudocódigo):
def visit(self, node):
    # Obtiene el nombre de la clase del nodo
    node_type = node.__class__.__name__  # "AddSubExprContext"
    
    # Construye el nombre del método
    method_name = f"visit{node_type}"    # "visitAddSubExprContext"
    
    # Llama dinámicamente al método
    method = getattr(self, method_name)
    return method(node)
```

### Flujo visual:

```
AST (Abstract Syntax Tree)
│
├── Program
│   └── visitProgram(ctx)
│       ├── Expr_stmt
│       │   └── visitExpr_stmt(ctx)
│       │       └── AddSub
│       │           └── visitAddSubExpr(ctx)
│       │               ├── NumExpr(5)
│       │               │   └── visitNumExpr(ctx)
│       │               │       → 5
│       │               │
│       │               └── MulDiv
│       │                   └── visitMulDivExpr(ctx)
│       │                       ├── NumExpr(3)
│       │                       │   └── 3
│       │                       └── NumExpr(2)
│       │                           └── 2
│       │                       → 6
│       │               → 11
│       │       → print(11)
```

---

## ESCENARIO 8: Cambios que puedes demostrar al profesor

### Cambio 1: Agregar contador de operaciones

**En `__init__`:**
```python
def __init__(self):
    super().__init__()
    self.memory = {}
    self.operation_count = 0  # ← NUEVO
    self.function_calls = 0    # ← NUEVO
```

**En cada operación:**
```python
def visitAddSubExpr(self, ctx):
    self.operation_count += 1
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))
    op = ctx.getChild(1).getText()
    return left + right if op == '+' else left - right

def visitFuncCallExpr(self, ctx):
    self.function_calls += 1
    # ... resto del código
```

**Al final en `main.py`:**
```python
visitor = TrezVisitor()
try:
    visitor.visit(tree)
    print(f"\nEstadísticas: {visitor.operation_count} operaciones, {visitor.function_calls} llamadas")
except TrezRuntimeError as e:
    print(f"\n❌ {e.msg}\n")
```

**Resultado:**
```
5 + 3 * 2;

11
Estadísticas: 2 operaciones, 0 llamadas
```

### Cambio 2: Debug mode

```python
class TrezVisitor(AntlrTrezVisitor):
    def __init__(self, debug=False):
        super().__init__()
        self.memory = {}
        self.debug = debug
    
    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        result = left + right if op == '+' else left - right
        
        if self.debug:
            print(f"[DEBUG] {left} {op} {right} = {result}")
        
        return result
```

**En `main.py`:**
```python
visitor = TrezVisitor(debug=True)  # ← ACTIVA DEBUG
```

**Resultado:**
```
5 + 3 * 2;

[DEBUG] 3 * 2 = 6
[DEBUG] 5 + 6 = 11
11
```

### Cambio 3: Manejo de errores mejorado

```python
def visitAddSubExpr(self, ctx):
    try:
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        
        if not isinstance(left, (int, float)):
            raise TrezRuntimeError(f"Operando izquierdo debe ser número, recibí {type(left).__name__}")
        if not isinstance(right, (int, float)):
            raise TrezRuntimeError(f"Operando derecho debe ser número, recibí {type(right).__name__}")
        
        op = ctx.getChild(1).getText()
        return left + right if op == '+' else left - right
    
    except TrezRuntimeError:
        raise
    except Exception as e:
        raise TrezRuntimeError(f"Error en suma/resta: {e}")
```

---

## ESCENARIO 9: Profesor pregunta "¿Cómo procesa TREZ un archivo Excel?"

### El flujo completo:

```trez
// 1. Cargar el Excel como lista de dicts
let datos = Datadoz.read_xlsx("../tests/data.xlsx");

// 2. Explorar estructura
mostrar(Datadoz.num_filas(datos));         // 10280
mostrar(Datadoz.columnas(datos));          // [id, edad, nivel_edu, ...]

// 3. Extraer columnas
let edades   = Datadoz.columna(datos, "edad");
let ingresos = Datadoz.columna(datos, "ingreso_mensual");

// 4. Calcular estadísticas en TREZ puro
let suma = 0;
for e in edades { let suma = suma + e; }
let media = suma / len(edades);
mostrar(media);   // 39.73

// 5. Graficar
Plotdoz.histogram(edades, "Distribución de Edades", "Edad", "Frecuencia", 30, "edades.png");
Plotdoz.scatter(edades, ingresos, "Edad vs Ingreso", "Edad", "Ingreso", "steelblue", "scatter.png");
```

### ¿Dónde está cada pieza?

| Paso | Archivo | Qué hace |
|------|---------|----------|
| `Datadoz.read_xlsx()` | `lib/datadoz/datadoz.py` | Abre el xlsx con openpyxl, retorna lista de dicts |
| `Datadoz.columna()` | `lib/datadoz/datadoz.py` | Extrae una columna como lista de valores |
| `Plotdoz.histogram()` | `lib/plotdoz/plotdoz.py` | Genera PNG con matplotlib (modo Agg, sin GUI) |
| Dispatch `Datadoz.*` | `visitor.py` `_NAMESPACES['Datadoz']` | Mapea nombre→función Python |
| Dispatch `Plotdoz.*` | `visitor.py` `_NAMESPACES['Plotdoz']` | Mapea nombre→función Python |

### ¿Por qué Datadoz y no IOdoz para leer el Excel?

IOdoz lee texto plano (strings). Datadoz maneja datos **estructurados**: infiere tipos, maneja cabeceras, retorna dicts. Es separación de responsabilidades: I/O genérico vs. datos tabulares para ML.

---

## ESCENARIO 10: Profesor pregunta "¿Cómo agregarías una gráfica de curva de pérdida?"

### Ya está implementada. Código de ejemplo:

```trez
// Simular losses de entrenamiento
let losses_train = [2.3, 1.8, 1.4, 1.1, 0.9, 0.7, 0.6, 0.5];
let losses_val   = [2.5, 2.0, 1.6, 1.3, 1.1, 0.9, 0.85, 0.82];

Plotdoz.learning_curve(
    losses_train,
    losses_val,
    "Learning Curve - Red Neuronal",
    "Epoch",
    "Loss",
    "learning_curve.png"
);
```

### ¿Dónde está implementada?

**Archivo:** `src/lib/plotdoz/plotdoz.py` función `learning_curve()`.

Dibuja la curva de train en azul y val en rojo discontinuo.
Si no hay `val_losses`, solo dibuja train. La imagen se guarda en el path indicado.

---

## TABLA RÁPIDA: ¿Dónde está cada cosa?

| Lo que pregunta el profesor | Archivo | Línea | Método |
|-----|---------|-------|--------|
| "¿Dónde se suman dos números?" | visitor.py | 207-208 | visitAddSubExpr |
| "¿Dónde se multiplica?" | visitor.py | 131-132 | visitMulDivExpr |
| "¿Dónde se divide?" | visitor.py | 133 | visitMulDivExpr |
| "¿Dónde se guardan variables?" | visitor.py | 24 | visitLet_stmt |
| "¿Dónde se recuperan variables?" | visitor.py | 38-39 | visitVarExpr |
| "¿Dónde se llaman funciones?" | visitor.py | 42-89 | visitFuncCallExpr |
| "¿Dónde se imprimen resultados?" | visitor.py | 29 | visitExpr_stmt |
| "¿Dónde se evalúan números?" | visitor.py | 213 | visitNumExpr |
| "¿Dónde se evalúan arrays?" | visitor.py | 116-119 | visitArray |
| "¿Dónde se manejan condicionales?" | visitor.py | 97-103 | visitIf_stmt |
| "¿Dónde están los bucles?" | visitor.py | 105-109 | visitWhile_stmt |
| "¿Dónde se calcula sin(x)?" | visitor.py + mathdoz/core_mathdoz.py | - | visitFuncCallExpr |
| "¿Dónde se controla precisión?" | visitor.py | 29 | visitExpr_stmt |
| "¿Cómo se lee un Excel?" | lib/datadoz/datadoz.py | - | read_xlsx() |
| "¿Cómo se lee un CSV?" | lib/datadoz/datadoz.py | - | read_csv() |
| "¿Cómo se grafíca?" | lib/plotdoz/plotdoz.py | - | bar_chart/histogram/scatter/learning_curve |
| "¿Dónde están los namespaces?" | visitor.py `_NAMESPACES` | ~50 | dict de lambdas |

---

**¡Con estos ejemplos puedes responder cualquier pregunta del profesor!** ✨
