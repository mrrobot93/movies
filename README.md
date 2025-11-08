# Movie Score Data Pipeline

This project implements an ETL (Extract, Transform, Load) pipeline to process and unify movie data from three different providers.

## Objective

The goal is to ingest data from CSV and JSON files, standardize it, merge it, and produce a unified Pandas DataFrame ready for analysis by the Data Science team.

## Structure

* `/src/providers.py`: Contains a dedicated class for each provider (CriticAggProvider, AudiencePulseProvider, BoxOfficeMetricsProvider). Each class handles the Extraction and Transformation logic for its specific source.
* `/src/orchestrator.py`: Contains the PipelineOrchestrator class, which directs the providers and handles the final merge logic.
* `/src/main.py`: This is the entry point that initializes and runs the pipeline, demonstrating the final result in a Pandas DataFrame.
* `/entrypoint.py`: The root script to launch the application.

## How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone [TU_URL_DE_GIT]
    cd MOVIES
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run:**
    El punto de entrada principal es `entrypoint.py`:
    ```bash
    python entrypoint.py
    ```

5.  **Test:**
    ```bash
    pytest
    ```

## Dependencies

* pandas
* pytest