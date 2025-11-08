import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.orchestrator import PipelineOrchestrator

def test_orchestrator_simple_merge_logic():
    """
    Tests the core _merge_data logic without running the full pipeline.
    """
    fake_paths = {
        'provider1': 'fake.csv',
        'provider2': 'fake.json',
        'provider3_domestic': 'fake.csv',
        'provider3_international': 'fake.csv',
        'provider3_financials': 'fake.csv'
    }
    orchestrator = PipelineOrchestrator(provider_paths=fake_paths)
    
    # Create two simple lists of data, like from two providers
    list_from_provider1 = [{'movie_title': 'Inception', 'release_year': 2010, 'critic_score': 87}]
    list_from_provider2 = [{'movie_title': 'Inception', 'release_year': 2010, 'audience_score': 9.1}]
    
    orchestrator._merge_data(list_from_provider1)
    orchestrator._merge_data(list_from_provider2)
    
    # Check that the data was merged in the orchestrator's state
    assert len(orchestrator.unified_data) == 1
    
    # Get the merged record
    key = ('Inception', 2010)
    merged_record = orchestrator.unified_data[key]
    
    # Check that it has data from BOTH lists
    assert merged_record['critic_score'] == 87
    assert merged_record['audience_score'] == 9.1