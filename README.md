# Análisis Exploratorio de Datos (EDA) de Videojuegos

Este proyecto realiza un Análisis Exploratorio de Datos (EDA) en un conjunto de datos de videojuegos. El objetivo es identificar patrones y tendencias clave que pueden ayudar a comprender mejor los factores que contribuyen al éxito de un videojuego.

## Descripción

El script de Python proporcionado realiza un EDA básico sobre un archivo CSV que contiene datos de videojuegos. Las funcionalidades incluyen la normalización de nombres de columnas, la verificación y eliminación de duplicados, y la generación de un resumen estadístico y visualizaciones de los datos.

## Características

El script incluye las siguientes características:
- Lectura de archivos CSV desde múltiples ubicaciones.
- Normalización de nombres de columnas para una manipulación de datos más fácil.
- Detección y eliminación de filas duplicadas.
- Generación de un resumen estadístico del conjunto de datos.
- Visualización de datos mediante histogramas y mapas de calor.
- Análisis de variables categóricas.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python y las siguientes bibliotecas:
- pandas
- matplotlib
- seaborn
- numpy

## Uso

Para ejecutar el análisis, necesitas tener un archivo CSV con datos de videojuegos. El archivo debe estar en el directorio de trabajo actual, o dentro de las carpetas `datasets` o `notebooks`. 

Ejecuta el script `EDA.py` con Python. Puedes modificar los parámetros en la función `execute_analysis` para personalizar el análisis según tus necesidades.

```bash
python EDA.py
