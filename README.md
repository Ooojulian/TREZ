# 🧠 TREZ Language


https://www.figma.com/make/RriKruOSSlTA1CcIjeTxWu/Mockups-para-sistema-de-sensores?fullscreen=1

**TREZ** es un lenguaje de programación de dominio específico (DSL) enfocado en Deep Learning, desarrollado completamente desde cero sin el uso de librerías externas para los cálculos matemáticos o de tensores (cero dependencias a NumPy, PyTorch, etc.). 

El lenguaje está diseñado bajo un **paradigma funcional** y utiliza el **patrón de diseño Visitor** para la evaluación de su Árbol Sintáctico Abstracto (AST).

## 🚀 Características Principales

*   **Sin Dependencias Externas:** Todos los cálculos matemáticos, estructuras de tensores, funciones de activación (ReLU, Sigmoid) y algoritmos de retropropagación están construidos nativamente.
*   **Paradigma Funcional:** Enfocado en funciones puras, inmutabilidad y evaluación de expresiones sin efectos secundarios.
*   **Patrón Visitor:** La ejecución del código se realiza recorriendo el AST generado mediante un diseño Visitor estructurado en Python.
*   **Enfoque en Deep Learning:** Capacidad para definir y entrenar redes neuronales, autoencoders y redes siamesas desde sintaxis nativa.
*   **Construido con ANTLR4:** Análisis léxico y sintáctico robusto compilado a Python.

## 🛠️ Requisitos del Sistema

*   **Python >= 3.10**
*   **ANTLR4** (Generador de parsers)
*   **Java JRE / JDK** (Requerido por la herramienta de generación de ANTLR4)

## 📦 Primera Entrega

La primera iteración del lenguaje permite el análisis y ejecución matemática básica:
*   Suma (`+`)
*   Resta (`-`)
*   Multiplicación (`*`)
*   División (`/`)
*   Soporte para jerarquía de operaciones usando paréntesis `()`.
