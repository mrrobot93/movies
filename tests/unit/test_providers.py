import sys
import os
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(project_root, 'src'))

from providers import CriticAggProvider, AudiencePulseProvider

def test_critic_agg_data_types(tmp_path):
    """
    """
    fake_csv_content = (
        "movie_title,release_year,critic_score_percentage,top_critic_score,total_critic_reviews_counted\n"
        "Inception,2010,87,8.1,450\n"
        "Parasite,2019,99,9.5,475"
    )
    fake_file_path = tmp_path / "test_provider1.csv"
    fake_file_path.write_text(fake_csv_content, encoding='utf-8')

    provider = CriticAggProvider(file_path=str(fake_file_path))
    result = provider.process()

    assert len(result) == 2

    inception_data = result[0]
    assert inception_data['movie_title'] == "Inception"
    assert isinstance(inception_data['release_year'], int)
    assert inception_data['release_year'] == 2010

    parasite_data = result[1]
    assert isinstance(parasite_data['top_critic_score'], float)
    assert parasite_data['top_critic_score'] == 9.5

def test_audience_pulse_data_types(tmp_path):
    """
    """
    # Define the fake JSON content
    fake_json_content = [
        {
            "title": "Inception",
            "year": "2010",
            "audience_average_score": 9.1,
            "total_audience_ratings": 1500000,
            "domestic_box_office_gross": 292576195
        },
        {
            "title": "The Dark Knight",
            "year": "2008",
            "audience_average_score": 9.4,
            "total_audience_ratings": 2200000,
            "domestic_box_office_gross": 533345358
        }
    ]
    
    # Create a fake JSON file for the test
    fake_file_path = tmp_path / "test_provider2.json"
    with open(fake_file_path, 'w', encoding='utf-8') as f:
        json.dump(fake_json_content, f)

    provider = AudiencePulseProvider(file_path=str(fake_file_path))
    result = provider.process()
    
    assert len(result) == 2 

    # Check data types for the first record ("Inception")
    inception_data = result[0]
    assert inception_data['movie_title'] == "Inception"
    assert isinstance(inception_data['release_year'], int)
    assert inception_data['release_year'] == 2010

    # Check data types for the second record ("The Dark Knight")
    dk_data = result[1]
    assert isinstance(dk_data['audience_average_score'], float)
    assert dk_data['audience_average_score'] == 9.4