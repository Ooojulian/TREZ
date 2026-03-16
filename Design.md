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

### Fase 1: Motor Matemático Base (Actual)
- [x] Gramática en ANTLR4 para parsing numérico.
- [x] Evaluación de operaciones aritméticas `+`, `-`, `*`, `/`.
- [x] Manejo de precedencia con paréntesis.
- [x] Implementación sólida del Visitor en Python.

### Fase 2: Estructuras Tensoriales y Funciones
- [ ] Definición de arreglos multidimensionales `[1, 2, 3]`.
- [ ] Operaciones de álgebra lineal básicas.
- [ ] Declaración de funciones puras (`func(x) -> x + 1`).

### Fase 3: Primitivas de Deep Learning
- [ ] Implementar funciones de activación matemáticamente: `ReLU`, `Sigmoid`, `Tanh`.
- [ ] Función de pérdida (Loss functions): `MSE`, `Categorical Crossentropy`.
- [ ] Implementación de un grafo computacional ligero para **Backpropagation** automático (AutoGrad casero).

### Fase 4: Arquitecturas Complejas de Red
- [ ] Soporte para **Redes Siamesas**.
- [ ] Implementación de **Autoencoders** (Codificación y Decodificación de entrada).
- [ ] Script completo entrenando una neurona para compuertas lógicas (XOR) usando TREZ.

## 4. Estructura de Proyecto Esperada

```text
TREZ/
├── README.md             <-- Contexto general e inicialización
├── Design.md             <-- (Este archivo) Documentación de arquitectura
├── src/
│   ├── Trez.g4           <-- Archivo de gramática ANTLR4
│   ├── main.py           <-- Punto de entrada del intérprete
│   ├── visitor.py        <-- Lógica funcional de evaluación matemática
│   └── math_engine.py    <-- Listas anidadas y cálculo algebraico
└── tests/                <-- Pruebas unitarias
```
