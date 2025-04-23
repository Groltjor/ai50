Este es el archivo README del modelo entrenado para el ejercicio Traffic del curso AI50, donde se utiliza un conjunto de imágenes de señalizaciones europeas para entrenar una red neuronal capaz de reconocerlas.

En este caso, utilizando la librería OpenCV, las imágenes se convierten en arreglos de NumPy y se redimensionan a 30x30 píxeles, con el objetivo de reducir la complejidad computacional y acelerar el procesamiento durante el entrenamiento.

Con TensorFlow, se construye una red neuronal convolucional que inicia con una capa Conv2D de 32 filtros, seguida por una capa MaxPooling2D para extraer y consolidar las características relevantes. Estas estrategias están inspiradas en las recomendaciones del curso AI50, y han demostrado ser efectivas para resolver el problema de clasificación de señales de tránsito.

Además, el uso de Dropout es crucial para reducir el riesgo de overfitting, permitiendo que el modelo generalice mejor a nuevas imágenes que no ha visto durante el entrenamiento.
