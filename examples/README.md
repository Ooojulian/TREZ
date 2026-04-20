# 📚 Ejemplos de TREZ

Este directorio contiene ejemplos progresivos del lenguaje TREZ, desde operaciones básicas hasta características avanzadas de Deep Learning.

## Estructura

| Archivo | Tema | Descripción |
|---------|------|-------------|
| `01_basic_math.trez` | Matemática Básica | Operaciones aritméticas y precedencia |
| `02_variables.trez` | Variables | Definición y uso de variables, constantes matemáticas |
| `03_arrays.trez` | Arrays/Tensores | Vectores, matrices, producto punto, transposición |
| `04_activation_functions.trez` | Activaciones | ReLU y Sigmoid para redes neuronales |
| `05_loss_functions.trez` | Funciones de Pérdida | MSE y su gradiente para entrenamiento |
| `06_math_functions.trez` | Funciones Matemáticas | Exponencial, logaritmo, trigonometría (sin dependencias) |
| `07_control_flow.trez` | Control de Flujo | If/else, while loops |
| `08_file_io.trez` | Entrada/Salida | Lectura y escritura de archivos |

## Cómo ejecutar

```bash
cd TREZ/src
python main.py ../examples/01_basic_math.trez
python main.py ../examples/02_variables.trez
# ... y así sucesivamente
```

## Características Destacadas de TREZ

### Sin Dependencias Externas ✨
- Toda la matemática está implementada nativamente
- Exponenciales y logaritmos usan series de Maclaurin
- Trigonometría mediante series de Taylor
- Raíces cuadradas con método Newton-Raphson

### Paradigma Funcional
- Enfoque en expresiones puras
- Minimización de efectos secundarios
- Evaluación mediante Visitor Pattern en AST

### Orientado a Deep Learning
- Funciones de activación: ReLU, Sigmoid
- Pérdida: MSE y su gradiente
- Operaciones tensoriales: dot product, transpose
- Preparado para autograd en futuras versiones

## Próximos Pasos

Los ejemplos avanzan según el roadmap de fases:
- **Fase 1** ✅ Operaciones aritméticas y variables
- **Fase 2** ✅ Estructuras tensoriales y funciones
- **Fase 3** 🚧 Primitivas de Deep Learning (autograd)
- **Fase 4** 🔮 Arquitecturas complejas (Redes Siamesas, Autoencoders)
