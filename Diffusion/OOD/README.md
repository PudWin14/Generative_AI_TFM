# Detección de imágenes Fuera de Distribución (OOD)
En esta carpeta, se encuentran los distintos notebooks utilizados para el entrenamiento, recolección de datos y la clasificación de imágenes OOD con modelos de Difusión.

El procedimiento seguido es el siguiente:
1. Entrenamiento del modelo base a utilizar. Notebook OOD_base_model.ipynb. Genera el fichero de pesos "Base_model_OOD_detection.pth"
2. Obtención de Distribución de datos en el modelo base, necesarios para calcular el z-score de las métricas realizadas. Para esto, realizamos N, 50 en este caso, restauraciones de cada imagen, cada una con un Timestep diferente, y calculamos las métricas que nos interesan, MSE y LPIPS. Notebook Get_base_distribution.ipynb. Se guardan los datos obtenidos en el fichero "Base_data.csv"
3. Con estos datos, calculamos la distribución estadística de cada métrica y para cada timestep, su media y desviación estándar. Notebook Distribution_of_metrics.ipynb. Se almacenan las distribuciones en "Base_data_distribution.csv"
4. Finalmente, con todos estos datos obtenidos, pasamos a realizar la detección de imágenes OOD. Notebook OOD_detection.ipynb
