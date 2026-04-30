# 🧠 TREZ: Guía Técnica Detallada para Preguntas del Profesor

## 1. ¿DÓNDE ESTÁ EL "CEREBRO" DEL PROYECTO?

### Respuesta: En `src/visitor.py` (líneas 11-227)

El **corazón del intérprete** es la clase `TrezVisitor`. Aquí fluye todo:

```
Código TREZ
    ↓
main.py (línea 30): tree = parser.program()
    ↓
visitor.py (línea 11): class TrezVisitor(AntlrTrezVisitor)
    ↓
visitor.visit(tree) [línea 40 en main.py]
    ↓
¡CEREBRO! Aquí se procesa cada nodo del AST
```

### La estructura mental:

**`visitor.py` contiene un método para CADA tipo de nodo:**

| Método | Qué hace | Línea |
|--------|----------|-------|
| `visitProgram` | Procesa el programa completo | 16-19 |
| `visitExpr_stmt` | Ejecuta una expresión y imprime | 27-30 |
| `visitLet_stmt` | Define variables (guarda en memory) | 21-25 |
| `visitAddSubExpr` | Suma y resta | 193-210 |
| `visitMulDivExpr` | Multiplicación y división | 121-136 |
| `visitFuncCallExpr` | Llama funciones (relu, sin, etc) | 42-89 |
| `visitNumExpr` | Convierte texto a número | 212-214 |

---

## 2. EL FLUJO ESPECÍFICO DE UNA OPERACIÓN SIMPLE

### Ejemplo: `5 + 3 * 2;`

```
Paso 1 - LEXER (Trezlexer.py, generado por ANTLR4):
  "5 + 3 * 2;" → [NUMBER(5), PLUS, NUMBER(3), MUL, NUMBER(2), SEMICOLON]

Paso 2 - PARSER (TrezParser.py, generado por ANTLR4):
  Crea AST respetando precedencia:
          AddSub
          /     \
        NUM(5)  MulDiv
                /     \
              NUM(3)  NUM(2)

Paso 3 - VISITOR (visitor.py, TÚ ESCRIBES ESTO):
  visitAddSubExpr() → izq = visit(NUM(5)) = 5
                      der = visit(MulDiv)
                           → visitMulDivExpr() = 3 * 2 = 6
                      → 5 + 6 = 11
```

**Código real en visitor.py:**

```python
def visitAddSubExpr(self, ctx: TrezParser.AddSubExprContext):    # Línea 193
    left = self.visit(ctx.expr(0))      # Visita izquierda: 5
    right = self.visit(ctx.expr(1))     # Visita derecha: 6
    op = ctx.getChild(1).getText()      # Obtiene el operador: "+"
    
    if op == '+':
        return left + right             # 5 + 6 = 11
    else:
        return left - right
```

---

## 3. ¿DÓNDE CONTROLAR LA PRECISIÓN DE DECIMALES?

### **OPCIÓN 1: En `visitExpr_stmt` (línea 27-30) - RECOMENDADA**

Aquí es donde se imprime el resultado:

```python
def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    print(result)  # ← AQUÍ CONTROLAS CÓMO SE MUESTRA
    return result
```

**CAMBIO PARA CONTROLAR DECIMALES:**

```python
def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    
    # Opción A: Mostrar máximo 4 decimales
    if isinstance(result, float):
        print(round(result, 4))
    else:
        print(result)
    
    return result
```

### **Ejemplo práctico:**

```
Código TREZ:
  15 / 3;

Sin cambio:
  5.0

Con round(result, 4):
  5.0

Código TREZ:
  10 / 3;

Sin cambio:
  3.3333333333333335

Con round(result, 4):
  3.3333
```

### **OPCIÓN 2: Crear una función de formateo personalizado**

Agregar al `visitor.py`:

```python
def format_output(self, value, decimals=4):
    """Formatea resultado con precisión controlada"""
    if isinstance(value, float):
        # Redondea a N decimales
        return round(value, decimals)
    elif isinstance(value, list):
        # Redondea cada elemento si es float
        return [round(x, decimals) if isinstance(x, float) else x for x in value]
    return value

def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    formatted = self.format_output(result, decimals=2)
    print(formatted)
    return result
```

### **OPCIÓN 3: Agregar variable global de precisión**

En `visitor.py` (línea 12):

```python
class TrezVisitor(AntlrTrezVisitor):
    def __init__(self):
        super().__init__()
        self.memory = {}
        self.precision = 4  # ← CONTROLA AQUÍ LA PRECISIÓN
```

Luego usas `self.precision` en cualquier lugar:

```python
def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    if isinstance(result, float):
        print(round(result, self.precision))
    else:
        print(result)
    return result
```

---

## 4. PARADIGMA FUNCIONAL EN EL CÓDIGO

### ¿DÓNDE ESTÁ EL PARADIGMA FUNCIONAL?

**Línea 14: `self.memory = {}`**

Esta es la clave del enfoque funcional:

```python
class TrezVisitor(AntlrTrezVisitor):
    def __init__(self):
        super().__init__()
        self.memory = {}  # ← AQUÍ: Vinculaciones inmutables (en teoría)
```

### Ejemplo: Variables como "bindings" funcionales

```python
def visitLet_stmt(self, ctx: TrezParser.Let_stmtContext):  # Línea 21
    var_name = ctx.ID().getText()      # Nombre: "x"
    value = self.visit(ctx.expr())     # Valor: 10 (evaluado)
    self.memory[var_name] = value      # BINDING: x ↦ 10
    return value
```

**Código TREZ:**
```
let x = 5;
let y = x + 3;
y;  // 8
```

**Ejecución:**
```
memory = {}
  ↓ visitLet_stmt("x")
memory = {"x": 5}
  ↓ visitLet_stmt("y")
    - y = visit(x + 3)
    - x = memory["x"] = 5
    - y = 5 + 3 = 8
memory = {"x": 5, "y": 8}
```

### ¿Dónde se ve la "pureza funcional"?

```python
def visitAddSubExpr(self, ctx: TrezParser.AddSubExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))
    # NO MODIFICA left ni right
    # RETORNA un nuevo valor
    return left + right  # ← PURO: entrada → salida, sin efectos secundarios
```

**CONTRASTE: Lo que NO hacemos (sería impuro):**

```python
# ESTO SERÍA IMPURO (modificar estado externo):
def visitAddSubExpr_impuro(self, ctx):
    self.memory["temp"] = self.visit(ctx.expr(0))  # ¡MALO! Efecto secundario
    self.memory["temp"] += self.visit(ctx.expr(1))
    return self.memory["temp"]
```

---

## 5. PATRÓN VISITOR EXPLICADO PASO A PASO

### ¿QUÉ ES EL PATRÓN VISITOR?

Es un patrón donde:
- Cada **tipo de nodo** tiene un método `visit[Tipo]()`
- El visitor "visita" cada nodo recursivamente
- Cada nodo sabe qué hacer según su tipo

### Flujo real:

```python
# main.py línea 38-40:
visitor = TrezVisitor()
try:
    visitor.visit(tree)  # ¡COMIENZA AQUÍ!
```

El `visit()` es mágico (viene de ANTLR):

```python
# ANTLR automáticamente hace:
def visit(self, node):
    # Si el nodo es AddSub → llama visitAddSubExpr
    # Si el nodo es NumExpr → llama visitNumExpr
    # Si el nodo es VarExpr → llama visitVarExpr
    # etc.
    method_name = f"visit{node.__class__.__name__}"
    return getattr(self, method_name)(node)
```

### Ejemplo visual:

```
            Program
              |
         Expr_stmt
              |
           AddSub
          /      \
        Num      MulDiv
        (5)      /    \
              Num    Num
              (3)    (2)

visitor.visit(Program)
  → visitProgram()
    → para cada stmt: visitor.visit(Expr_stmt)
      → visitExpr_stmt()
        → visitor.visit(AddSub)
          → visitAddSubExpr()
            → left = visitor.visit(Num) → visitNumExpr() → 5
            → right = visitor.visit(MulDiv)
              → visitMulDivExpr()
                → left = visitor.visit(Num) → 3
                → right = visitor.visit(Num) → 2
                → 3 * 2 = 6
            → 5 + 6 = 11
```

---

## 6. PREGUNTAS ESPECÍFICAS DEL PROFESOR + RESPUESTAS

### P: "¿Dónde se manejan los números flotantes?"

**R:** En `visitNumExpr` (línea 212-214):

```python
def visitNumExpr(self, ctx: TrezParser.NumExprContext):
    val = ctx.getText()  # "3.14" o "5"
    return float(val) if '.' in val else int(val)
    # ↑ Si tiene punto → float, si no → int
```

**Si dividimos:** `15 / 3.0` → `visitMulDivExpr` (línea 133):
```python
elif op == '/':
    return left / right  # 15 / 3.0 = 5.0 (siempre float)
```

### P: "¿Cómo puedo cambiar que `5.0` se muestre como `5`?"

**R:** En `visitExpr_stmt` (línea 27-30):

```python
def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    
    # Si es entero disfrazado de float, muéstralo como int
    if isinstance(result, float) and result.is_integer():
        print(int(result))
    else:
        print(result)
    
    return result
```

### P: "¿Dónde está el manejo de arrays?"

**R:** En `visitArrayExpr` (línea 111-119):

```python
def visitArrayExpr(self, ctx: TrezParser.ArrayExprContext):
    return self.visit(ctx.array())

def visitArray(self, ctx: TrezParser.ArrayContext):
    items = []
    for expr_ctx in ctx.expr():
        items.append(self.visit(expr_ctx))
    return items  # Lista de Python
```

**Código TREZ:** `[1, 2, 3];` → Python: `[1, 2, 3]`

### P: "¿Cómo se procesan las funciones como `sin(x)`?"

**R:** En `visitFuncCallExpr` (línea 42-89):

```python
def visitFuncCallExpr(self, ctx: TrezParser.FuncCallExprContext):
    func_name = ctx.ID().getText()  # "sin"
    args = [self.visit(expr_ctx) for expr_ctx in ctx.expr()]  # [valor_de_x]
    
    # Dispatch (¿cuál función ejecutar?)
    elif func_name == 'sin':
        return math_utils.sin(args[0])  # Delega a sin() en math/core.py
```

**Flujo:** `sin(PI / 2)` 
```
visitFuncCallExpr
  ↓ func_name = "sin"
  ↓ args = [visit(PI / 2)]
    - visit(DIVIDE)
      - left = visit(VAR "PI") = 3.14159...
      - right = visit(NUM "2") = 2
      - 3.14159 / 2 = 1.5708...
  ↓ math_utils.sin(1.5708)
  → (calcula sin usando serie de Taylor en math/core.py)
  → 1.0
```

### P: "¿Dónde se hace la retropropagación?"

**R:** Aún NO existe en el código actual. Está en `autograd.py` (línea 80) pero incompleto.

Lo que SÍ existe es `mse_grad()` en `lib/losses/losses.py`:

```python
def mse_grad(y_true, y_pred):
    # Gradiente = 2 * (y_pred - y_true) / n
    return [2 * (p - t) / n for t, p in zip(y_true, y_pred)]
```

En `visitFuncCallExpr` (línea 58-59):
```python
elif func_name == 'mse_grad':
    return math_utils.mse_grad(args[0], args[1])
```

**Para Fase 3 necesitarías:**
```python
# autograd.py (a expandir)
class ComputationGraph:
    def __init__(self):
        self.nodes = []
        self.gradients = {}
    
    def backward(self, loss):
        # Recorre el grafo hacia atrás
        # Calcula gradientes para cada variable
        pass
```

---

## 7. RESPUESTAS CORTAS PARA PREGUNTAS RÁPIDAS

| Pregunta | Respuesta | Línea |
|----------|-----------|-------|
| ¿Dónde está el interpretador? | `visitor.py` clase `TrezVisitor` | 11 |
| ¿Dónde se evalúan números? | `visitNumExpr()` | 212 |
| ¿Dónde se suma? | `visitAddSubExpr()` | 193 |
| ¿Dónde se multiplica? | `visitMulDivExpr()` | 121 |
| ¿Dónde se llaman funciones? | `visitFuncCallExpr()` | 42 |
| ¿Dónde se guarden variables? | `self.memory` dict | 14 |
| ¿Dónde se controla precisión? | `visitExpr_stmt()` print | 29 |
| ¿Dónde se hallan errores? | `error_listener.py` | - |
| ¿Dónde está la gramática? | `src/parser/Trez*.py` (ANTLR) | - |
| ¿Dónde están las funciones math? | `src/lib/math/core.py` | - |

---

## 8. CAMBIOS PRÁCTICOS QUE PUEDES MOSTRAR

### Cambio 1: Mostrar máximo 3 decimales

**Archivo:** `src/visitor.py` línea 27-30

```python
# ANTES
def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    print(result)
    return result

# DESPUÉS
def visitExpr_stmt(self, ctx: TrezParser.Expr_stmtContext):
    result = self.visit(ctx.expr())
    if isinstance(result, float):
        print(round(result, 3))
    else:
        print(result)
    return result
```

### Cambio 2: Contar operaciones realizadas

**Agregue a `__init__` (línea 12-14):**

```python
def __init__(self):
    super().__init__()
    self.memory = {}
    self.operation_count = 0  # ← NUEVO
```

**Agregue en `visitAddSubExpr` (línea 193):**

```python
def visitAddSubExpr(self, ctx: TrezParser.AddSubExprContext):
    self.operation_count += 1  # ← CONTADOR
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))
    # ...
```

### Cambio 3: Debug mode

```python
class TrezVisitor(AntlrTrezVisitor):
    def __init__(self, debug=False):
        super().__init__()
        self.memory = {}
        self.debug = debug
    
    def visitAddSubExpr(self, ctx: TrezParser.AddSubExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        result = left + right if op == '+' else left - right
        
        if self.debug:
            print(f"DEBUG: {left} {op} {right} = {result}")
        
        return result
```

---

**¡Ahora puedes responder cualquier pregunta técnica del profesor!** 🚀
