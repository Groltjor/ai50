# 🧩 Crossword Solver

Este ejercicio representa el reto final de la serie de algoritmos clásicos en el curso de IA. Es uno de los más desafiantes, ya que requiere la integración de múltiples técnicas de resolución de restricciones para llenar correctamente un tablero de crucigrama a partir de un conjunto dado de palabras.

---

## 🧠 Algoritmos utilizados

- **AC-3 (Arc Consistency Algorithm 3)**  
  Para reducir dominios y garantizar consistencia entre variables antes de realizar una búsqueda.

- **Backtracking (con heurísticas opcionales)**  
  Para explorar posibles asignaciones de palabras a celdas, con retroceso inteligente.

- **Recursividad**  
  Utilizada como base para la búsqueda y propagación de restricciones.

---

## 🎯 Objetivo

Llenar un tablero de crucigrama de forma consistente con el conjunto de palabras proporcionado, cumpliendo todas las restricciones de espacio, intersecciones y longitud.

En caso de que no exista una solución válida, el programa debe detectarlo y notificarlo correctamente.

---

## 📌 Nota

La interfaz visual y el entorno del tablero fueron desarrollados por **Harvard University** como parte del curso [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/).

👨‍💻 **El rol del estudiante es implementar los algoritmos AC-3 y Backtracking**, así como la lógica necesaria para construir y resolver el crucigrama.

---

## 🛠️ Tecnologías utilizadas

- Python 3.x
- Algoritmos de resolución de restricciones
- Visualización proporcionada por Harvard
