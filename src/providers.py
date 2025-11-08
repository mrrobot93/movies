import csv
from typing import List, Dict

class CriticAggProvider:
    """
    'CriticAgg' Provider
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def process(self) -> List[Dict]:
        """
        """
        processed_data = []

        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    try:
                        transformed_row = {
                            'movie_title': row['movie_title'],
                            'release_year': int(row['release_year']),
                            'critic_score_percentage': int(row['critic_score_percentage']),
                            'top_critic_score': float(row['top_critic_score']),
                            'total_critic_reviews_counted': int(row['total_critic_reviews_counted'])
                        }
                        processed_data.append(transformed_row)
                    except (ValueError, KeyError) as e:
                        print(f"Error processing: {row}. Error: {e}")

        except FileNotFoundError:
            print(f"Error: File not found {self.file_path}")
            return []
        except Exception as e:
            print(f"Error: {e}")
            return []

        return processed_data