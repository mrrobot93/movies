from .providers import CriticAggProvider, AudiencePulseProvider

def main():
    print("Init")
    provider1_path = 'data/provider1.csv'
    critic_agg = CriticAggProvider(file_path=provider1_path)
    critic_data = critic_agg.process()

    if critic_data:
        print(f"CriticAgg Rows Processed: {len(critic_data)}")

    provider2_path = 'data/provider2.json'
    audience_pulse = AudiencePulseProvider(file_path=provider2_path)
    audience_data = audience_pulse.process()

    if audience_data:
        print(f"AudiencePulse Rows Processed: {len(audience_data)}")

if __name__ == "__main__":
    main()