# 🎮 Ejercicio: Tic-Tac-Toe (tradicionalmente conocido como "Gato")

Este ejercicio consiste en implementar la lógica necesaria para que un agente pueda jugar de forma óptima al clásico juego de Tic-Tac-Toe, utilizando el algoritmo **Minimax**.

El objetivo principal es construir un agente que, dados los posibles estados del juego, pueda tomar decisiones óptimas evaluando movimientos futuros hasta una **profundidad "n"**. Esto permite optimizar el rendimiento evitando una sobrecarga computacional.

## Comportamiento esperado del agente

- El agente debe **nunca perder**: su estrategia debe garantizar al menos un empate contra cualquier oponente.
- En escenarios favorables, debe **aprovechar para ganar**.
- Utiliza Minimax con recursividad y poda (si se desea mejorar).

## Nota importante

La implementación de la interfaz gráfica con **Pygame** fue desarrollada por **Harvard University** como parte del curso [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/).

**La tarea del estudiante es implementar únicamente el algoritmo Minimax**, asegurando que el agente actúe de forma racional.

## Tecnologías utilizadas

- Python 3.x
- Pygame (interfaz gráfica)
- Lógica de Minimax (implementación propia)
