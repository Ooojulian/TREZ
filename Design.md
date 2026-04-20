# 📐 Arquitectura y Diseño de TREZ

Este documento describe la planificación teórica y técnica del lenguaje de programación **TREZ**.

## 1. Visión General del Proyecto
**TREZ** es un lenguaje orientado a la creación, entrenamiento y ejecución de modelos de Inteligencia Artificial (especialmente Deep Learning) desde sus fundamentos matemáticos. Para lograr esto sin herramientas externas de terceros, el lenguaje incluye su propio motor de procesamiento tensorial.

## 2. Decisiones de Diseño Arquitectónico

### 2.1 Paradigma Funcional
El lenguaje fomenta escribir código sin efectos secundarios (side-effects). En lugar de modificar datos, las operaciones devuelven nuevas versiones de las estructuras. Esto es especialmente útil en Data Science y Deep Learning para manejar el flujo de tensores a través de una red.

### 2.2 Patrón Visitor para la Evaluación (Interpreter)
En lugar de compilar a código máquina o bytecode, TREZ será procesado como un árbol AST (Abstract Syntax Tree) generado por ANTLR4.
*   **Lexer y Parser:** ANTLR4 leerá el código fuente de los archivos `.trez` basándose en reglas gramaticales y generará el AST.
*   **Visitor Engine:** Un script principal en Python implementará el patrón Visitor (`TrezVisitor`), el cual recorrerá progresivamente cada nodo del árbol (Ej. `AddNode`, `MulNode`, `FunctionDefNode`) realizando el cómputo en crudo.

### 2.3 Cero Liberías Externas
El núcleo matemático de TREZ se creará "from scratch". 
*   **Tensores:** Implementados usando listas anidadas nativas de Python.
*   **Operaciones:** Se programarán algoritmos nativos para producto punto, transposición de matrices, y convolución.

## 3. Hoja de Ruta (Roadmap) y Alcance

### Fase 1: Motor Matemático Base ✅ COMPLETADA
- [x] Gramática en ANTLR4 para parsing numérico y control de flujo.
- [x] Evaluación de operaciones aritméticas `+`, `-`, `*`, `/`, `%`.
- [x] Manejo de precedencia con paréntesis.
- [x] Implementación sólida del Visitor en Python.
- [x] Variables con `let` y condicionales `if/else`.
- [x] Bucles `while`.
- [x] Soporte para strings.

### Fase 2: Estructuras Tensoriales y Funciones ✅ COMPLETADA
- [x] Definición de arreglos multidimensionales `[1, 2, 3]`.
- [x] Operaciones de álgebra lineal: `dot()` (producto punto), `transpose()`.
- [x] Operaciones escalares sobre tensores (ej. `learning_rate * array`).
- [x] **Funciones de activación:** `relu()`, `sigmoid()` (todas nativas).
- [x] **Funciones de pérdida:** `mse()`, `mse_grad()`.
- [x] **Entrada/Salida:** `leer()`, `escribir()` para archivos.
- [x] **Funciones matemáticas nativas:**
  - Algebraicas: `abs()`, `pow()`, `sqrt()`, `factorial()`
  - Trascendentales: `exp()`, `log()` (series de Maclaurin)
  - Trigonometría: `sin()`, `cos()`, `tan()` (series de Taylor)
- [x] Constantes: `PI`, `E`

### Fase 3: Primitivas de Deep Learning 🚧 EN PROGRESO
- [x] Funciones de activación matemáticamente: `ReLU`, `Sigmoid`
- [x] Función de pérdida: `MSE` y su gradiente
- [ ] Autograd (Automatic Differentiation) para backpropagation
- [ ] Capas de red (Layer abstraction)
- [ ] Optimizadores (SGD, Adam)

### Fase 4: Arquitecturas Complejas de Red 🔮 PLANIFICADA
- [ ] Soporte para **Redes Siamesas** (twin networks).
- [ ] Implementación de **Autoencoders** (Codificación y Decodificación).
- [ ] Script de ejemplo: XOR Solver usando descenso de gradiente.

## 4. Estructura de Proyecto

```text
TREZ/
├── README.md                    # Documentación principal
├── Design.md                    # (Este archivo) Arquitectura técnica
│
├── src/
│   ├── main.py                  # Punto de entrada del intérprete
│   ├── visitor.py               # Motor Visitor para evaluación de AST
│   ├── math_utils.py            # Punto de acceso para librerías matemáticas
│   ├── errors.py                # Definiciones de errores personalizados
│   ├── error_listener.py        # Captura de errores del parser ANTLR4
│   ├── autograd.py              # Grafo computacional para backprop (WIP)
│   │
│   ├── parser/                  # Código generado por ANTLR4
│   │   ├── TrezLexer.py
│   │   ├── TrezParser.py
│   │   ├── TrezParserVisitor.py
│   │   └── TrezParserListener.py
│   │
│   └── lib/                      # Librerías modulares (sin dependencias)
│       ├── math/
│       │   ├── core.py          # Funciones algebraicas y trascendentales
│       │   ├── tensor.py        # Operaciones tensoriales (dot, transpose)
│       │   └── __init__.py
│       │
│       ├── activations/         # Funciones de activación para NN
│       │   ├── activations.py
│       │   └── __init__.py
│       │
│       ├── losses/              # Funciones de pérdida para entrenamiento
│       │   ├── losses.py
│       │   └── __init__.py
│       │
│       └── io/                  # Entrada/salida de archivos
│           ├── io.py
│           └── __init__.py
│
├── examples/                     # Ejemplos progresivos de uso
│   ├── 01_basic_math.trez
│   ├── 02_variables.trez
│   ├── 03_arrays.trez
│   ├── 04_activation_functions.trez
│   ├── 05_loss_functions.trez
│   ├── 06_math_functions.trez
│   ├── 07_control_flow.trez
│   ├── 08_file_io.trez
│   └── README.md
│
└── tests/                        # Suite de tests exhaustiva
    ├── test_math_core.py        # Tests de funciones matemáticas
    ├── test_tensor_operations.py # Tests de álgebra lineal
    ├── test_activations.py       # Tests de activaciones
    ├── test_losses.py            # Tests de funciones de pérdida
    │
    ├── features/                # Tests de características del lenguaje
    │   ├── test_basic.trez
    │   ├── test_math.trez
    │   ├── test_backprop.trez
    │   ├── test_dl.trez
    │   └── test_io.trez
    │
    ├── syntax/                  # Tests de errores sintácticos
    │   └── test_syntax_error.trez
    │
    └── runtime/                 # Tests de errores en tiempo de ejecución
        └── test_runtime_error.trez
```

## 5. Implementación Técnica

### 5.1 Funciones Matemáticas Nativas

Todas las funciones trascendentales se implementan usando **series matemáticas**:

- **Exponencial:** Serie de Maclaurin: e^x = 1 + x + x²/2! + x³/3! + ...
- **Logaritmo:** Serie de Mercator centrada con ajuste de rango para precisión
- **Trigonometría:** Series de Taylor para sin(x), cos(x)
- **Raíz cuadrada:** Método de Newton-Raphson iterativo

### 5.2 Arquitectura del Motor

```
Código TREZ (.trez)
        ↓
   ANTLR4 Lexer
        ↓
   ANTLR4 Parser → Genera AST
        ↓
  TrezVisitor (Patrón Visitor)
        ↓
   Evaluación funcional
        ↓
   Resultado / Salida
```

### 5.3 Filosofía de Diseño

1. **Pureza Funcional:** Aunque Python permite side-effects, TREZ promueve expresiones puras
2. **Cero Dependencias:** El código matemático no depende de librerías externas
3. **Escalabilidad:** La arquitectura permite fácil extensión de nuevas funciones
4. **Claridad:** Nombres simples sin sufijos (se removió "_doz")
