from .providers import CriticAggProvider, AudiencePulseProvider, BoxOfficeMetricsProvider

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

    provider3_paths = {
        'domestic_path': 'data/provider3_domestic.csv',
        'international_path': 'data/provider3_international.csv',
        'financials_path': 'data/providers3_financials.csv'
    }
    
    box_office_metrics = BoxOfficeMetricsProvider(**provider3_paths)
    box_office_data = box_office_metrics.process()
    
    if box_office_data:
        print(f"BoxOfficeMetrics Rows Processed: {len(box_office_data)}")
        
        for movie in box_office_data:
            if movie.get('movie_title') == 'Inception':
                print(movie)
                break

if __name__ == "__main__":
    main()