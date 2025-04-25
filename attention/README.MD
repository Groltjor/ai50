# 🧠 Attention Mechanism (Inspirado en el paper de Google)

Este proyecto explora el mecanismo de **atención** en redes neuronales, una arquitectura clave en modelos de lenguaje natural como los Transformers.

El sistema de atención permite que una red neuronal enfoque dinámicamente su "atención" en tokens específicos de una secuencia de entrada, en lugar de procesarla de forma uniforme. Esta capacidad es fundamental en modelos como **BERT**, que logran contextualizar cada palabra en función de su entorno.

## Objetivo

Implementar y visualizar el comportamiento del mecanismo de atención utilizando:

- `TensorFlow`
- `Transformers` (Hugging Face)
- `NumPy`

## ¿Qué hace este proyecto?

- Utiliza **BERT** para realizar tareas de predicción de texto enmascarado (masked language modeling).
- Extrae los mapas de atención generados por el modelo.
- Visualiza gráficamente cómo el modelo "presta atención" a ciertos tokens mediante imágenes (`.png`).

## Resultado

Se generan visualizaciones que muestran **cómo BERT distribuye su atención** entre los tokens de entrada, lo cual ayuda a interpretar el comportamiento del modelo.

## Requisitos

- Python 3.9.22 (crucial para poder usar TF)
- TensorFlow
- transformers (Hugging Face)
- NumPy
- matplotlib o seaborn (para graficar)

## ✨ Inspiración

Este ejercicio está inspirado en el paper original de Google:  
📄 *Attention is All You Need* (Vaswani et al., 2017)
