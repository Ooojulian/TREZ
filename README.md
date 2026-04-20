# 🧠 TREZ Language

**TREZ** es un lenguaje de programación de dominio específico (DSL) enfocado en Deep Learning, desarrollado completamente desde cero sin el uso de librerías externas para los cálculos matemáticos o de tensores (cero dependencias a NumPy, PyTorch, etc.).

El lenguaje está diseñado bajo un **paradigma funcional** y utiliza el **patrón de diseño Visitor** para la evaluación de su Árbol Sintáctico Abstracto (AST).

## 🚀 Características Principales

- **Sin Dependencias Externas:** Todos los cálculos matemáticos, estructuras de tensores, funciones de activación (ReLU, Sigmoid) y algoritmos de retropropagación están construidos nativamente usando series matemáticas.
- **Paradigma Funcional:** Enfocado en funciones puras, inmutabilidad y evaluación de expresiones sin efectos secundarios.
- **Patrón Visitor:** La ejecución del código se realiza recorriendo el AST generado mediante un diseño Visitor estructurado en Python.
- **Enfoque en Deep Learning:** Capacidad para definir y entrenar redes neuronales, autoencoders y redes siamesas desde sintaxis nativa.
- **Construido con ANTLR4:** Análisis léxico y sintáctico robusto compilado a Python.

## 📖 Ejemplos Rápidos

### Operaciones Básicas
```trez
// Matemática simple
5 + 3 * 2;      // 11 (respeta precedencia)

// Variables
let x = 10;
let y = x * 2;  // 20
```

### Arrays y Tensores
```trez
let v1 = [1, 2, 3];
let v2 = [4, 5, 6];

// Producto punto
dot(v1, v2);           // 32

// Matriz y transposición
let M = [[1, 2], [3, 4]];
transpose(M);          // [[1, 3], [2, 4]]
```

### Funciones Matemáticas (Sin NumPy)
```trez
// Todas estas funciones se implementan desde cero
sqrt(16);              // 4
pow(2, 3);             // 8
exp(1);                // 2.718 (= E)
log(E);                // 1
sin(PI / 2);           // 1
cos(0);                // 1
```

### Deep Learning
```trez
// Activaciones
relu([1, -2, 3]);           // [1, 0, 3]
sigmoid(0);                 // 0.5

// Pérdida (Loss)
let y_true = [0, 1, 0];
let y_pred = [0.1, 0.9, 0.2];
mse(y_true, y_pred);        // Error Cuadrático Medio
mse_grad(y_true, y_pred);   // Gradiente para retropropagación
```

Más ejemplos en `/examples` - [Ver directorio de ejemplos](./examples)

## 🛠️ Requisitos del Sistema

- **Python >= 3.10**
- **ANTLR4** (Generador de parsers)
- **Java JRE / JDK** (Requerido por ANTLR4)

## 📦 Estado del Proyecto

**Fase 1** ✅ Operaciones aritméticas, variables, control de flujo
**Fase 2** ✅ Estructuras tensoriales, funciones de activación, pérdida
**Fase 3** 🚧 Autograd y retropropagación automática
**Fase 4** 🔮 Arquitecturas complejas (Redes Siamesas, Autoencoders)

## 📚 Documentación

- [Design.md](./Design.md) - Arquitectura técnica y decisiones de diseño
- [examples/README.md](./examples/README.md) - Guía de ejemplos progresivos
- [tests/](./tests/) - Suite de tests exhaustiva
