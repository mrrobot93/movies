# Movie Score Data Pipeline

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) para procesar y unificar datos de películas de tres proveedores diferentes

## Objetivo

El objetivo es ingerir datos de archivos CSV y JSON, estandarizarlos, unirlos y producir un DataFrame de Pandas unificado listo para el análisis del equipo de Data Science.

## Estructura

* `/src/providers.py`: Contiene una clase dedicada para cada proveedor (`CriticAggProvider`, `AudiencePulseProvider`, `BoxOfficeMetricsProvider`). Cada clase maneja la lógica de Extracción y Transformación para su fuente específica.
* `/src/orchestrator.py`: Contiene la clase `PipelineOrchestrator`, que dirige a los proveedores y maneja la lógica de **fusión (merge)** final.
* `/src/main.py`: Es el punto de entrada que inicializa y ejecuta el pipeline, y demuestra el resultado final en un DataFrame de Pandas.
* `/entrypoint.py`: Script raíz para lanzar la aplicación.

## Cómo Ejecutar el Proyecto

1.  **Clonar el repositorio:**
    ```bash
    git clone [TU_URL_DE_GIT]
    cd MOVIES
    ```

2.  **Crear un entorno virtual (Recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar el pipeline:**
    El punto de entrada principal es `entrypoint.py`:
    ```bash
    python entrypoint.py
    ```

5.  **Ejecutar las pruebas:**
    ```bash
    pytest
    ```

## Dependencias

* pandas
* pytest