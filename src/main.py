from .orchestrator import PipelineOrchestrator
import pandas as pd 

def main():
    print("Init...")

    all_paths = {
        'provider1': 'data/provider1.csv',
        'provider2': 'data/provider2.json',
        'provider3_domestic': 'data/provider3_domestic.csv',
        'provider3_international': 'data/provider3_international.csv',
        'provider3_financials': 'data/provider3_financials.csv'
    }

    orchestrator = PipelineOrchestrator(provider_paths=all_paths)
    final_data = orchestrator.run_pipeline()

    df = pd.DataFrame(final_data)

    print(df.head())

    print("\n--- Información del DataFrame (df.info()) ---")
    df.info()

if __name__ == "__main__":
    main()