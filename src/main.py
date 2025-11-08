from .providers import CriticAggProvider

def main():
    print("Init")
    provider1_path = 'data/provider1.csv'
    
    critic_agg = CriticAggProvider(file_path=provider1_path)
    critic_data = critic_agg.process()

    if critic_data:
        print(f"CriticAgg Rows Processed: {len(critic_data)}")

if __name__ == "__main__":
    main()