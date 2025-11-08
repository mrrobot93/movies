import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(project_root, 'src'))

from providers import CriticAggProvider

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