from typing import List, Dict, Tuple
from .providers import CriticAggProvider, AudiencePulseProvider, BoxOfficeMetricsProvider

class PipelineOrchestrator:
    """
    Orchestrator:
    1. get info of providers
    2. merge data
    """
    
    def __init__(self, provider_paths: Dict[str, str]):
        self.provider_paths = provider_paths
        
        # Init Providers
        self.critic_agg = CriticAggProvider(
            file_path=self.provider_paths['provider1']
        )
        self.audience_pulse = AudiencePulseProvider(
            file_path=self.provider_paths['provider2']
        )
        self.box_office_metrics = BoxOfficeMetricsProvider(
            domestic_path=self.provider_paths['provider3_domestic'],
            international_path=self.provider_paths['provider3_international'],
            financials_path=self.provider_paths['provider3_financials']
        )
        
        # Unified data
        self.unified_data: Dict[Tuple[str, int], Dict] = {}

    def run_pipeline(self) -> List[Dict]:
        """
        """
        print("Init ...")
        
        # --- Process Providers ---
        critic_data = self.critic_agg.process()
        audience_data = self.audience_pulse.process()
        box_office_data = self.box_office_metrics.process()
        
        # --- Merging data ---
        print("Merging...")
        
        self._merge_data(critic_data)
        self._merge_data(audience_data)
        self._merge_data(box_office_data)
        
        print(f"Final. {len(self.unified_data)} movies merged.")
        
        return list(self.unified_data.values())

    def _merge_data(self, data_list: List[Dict]):
        """
        """
        for movie_record in data_list:
            try:
                key = (movie_record['movie_title'], movie_record['release_year'])
                
                if key not in self.unified_data:
                    self.unified_data[key] = movie_record
                else:
                    self.unified_data[key].update(movie_record)
                    
            except KeyError:
                print(f"Merging Error: {movie_record}")
            except Exception as e:
                print(f"Error: {movie_record}: {e}")