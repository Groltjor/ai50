# 🧬 Heredity: Inferencia con Redes Bayesianas

Este ejercicio implementa una **red bayesiana** para inferir la probabilidad de que una persona posea un gen (o lo exprese mediante una característica observable) en función de la información genética de sus familiares.

---

## 🎯 Objetivo

Utilizar **lógica bayesiana** para modelar probabilísticamente:

- La **herencia genética** entre padres e hijos.
- La **probabilidad de expresión de un rasgo** en base a si una persona tiene 0, 1 o 2 copias de un gen.

---

## 🧠 ¿Qué hace el modelo?

Dado un conjunto de personas, sus relaciones familiares y (opcionalmente) si expresan una característica genética, el modelo:

- Estima la probabilidad de que cada persona tenga 0, 1 o 2 copias del gen.
- Calcula la probabilidad de que expresen el rasgo (por ejemplo, una enfermedad o una característica física).
- Toma en cuenta **mutaciones genéticas espontáneas**.

---

## 📌 Nota

Este ejercicio forma parte del curso [CS50's Introduction to Artificial Intelligence with Python – Harvard](https://cs50.harvard.edu/ai/).

👨‍💻 El rol del alumno es implementar las funciones de cálculo bayesiano que permiten inferir las probabilidades basadas en múltiples combinaciones posibles de genes.

---

## 🛠️ Tecnologías utilizadas

- Python 3.x
- Programación lógica y combinatoria
- Conceptos de inferencia probabilística
