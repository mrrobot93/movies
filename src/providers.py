import csv
import json
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


class AudiencePulseProvider:
    """
    'AudiencePulse' Provider
    """
    
    def __init__(self, file_path: str):
        self.file_path = file_path

    def process(self) -> List[Dict]:
        """
        """
        processed_data = []

        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                
                for row in data:                        
                    try:
                        transformed_row = {
                            'movie_title': row['title'],
                            'release_year': int(row['year']),
                            'audience_average_score': float(row['audience_average_score']),
                            'total_audience_ratings': int(row['total_audience_ratings']),
                            'domestic_box_office_gross': float(row['domestic_box_office_gross'])
                        }
                        processed_data.append(transformed_row)
                    except (ValueError, KeyError, TypeError) as e:
                        print(f"Error processing: {row}. Error: {e}")
                        
        except FileNotFoundError:
            print(f"Error: File not found {self.file_path}")
            return []
        except json.JSONDecodeError:
            print(f"Error: JSON corrupted {self.file_path}")
            return []
        except Exception as e:
            print(f"Error: {e}")
            return []
            
        return processed_data

class BoxOfficeMetricsProvider:
    """
    'BoxOfficeMetrics' Provider
    """
    
    def __init__(self, domestic_path: str, international_path: str, financials_path: str):
        self.domestic_path = domestic_path
        self.international_path = international_path
        self.financials_path = financials_path

    def process(self) -> List[Dict]:
        """
        """
        unified_data = {}

        try:
            with open(self.domestic_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        title = row['film_name']
                        year = int(row['year_of_release'])
                        key = (title, year)
                        
                        unified_data[key] = {
                            'movie_title': title,
                            'release_year': year,
                            'domestic_box_office_gross': float(row['box_office_gross_usd'])
                        }
                    except (ValueError, KeyError, TypeError) as e:
                        print(f"Error processing: {row}. Error: {e}")

            with open(self.international_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        title = row['film_name']
                        year = int(row['year_of_release'])
                        key = (title, year)

                        if key not in unified_data:
                            unified_data[key] = {'movie_title': title,'release_year': year}

                        unified_data[key]['international_box_office_gross'] = float(row['box_office_gross_usd'])
                    
                    except (ValueError, KeyError, TypeError) as e:
                        print(f"Error processing: {row}. Error: {e}")

            with open(self.financials_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:                    
                    try:
                        title = row['film_name']
                        year = int(row['year_of_release'])
                        key = (title, year)

                        if key not in unified_data:
                            unified_data[key] = {'movie_title': title,'release_year': year}
                        
                        unified_data[key]['production_budget_usd'] = float(row['production_budget_usd'])
                        unified_data[key]['marketing_spend_usd'] = float(row['marketing_spend_usd'])
                    
                    except (ValueError, KeyError, TypeError) as e:
                        print(f"Error processing: {row}. Error: {e}")
        
        except FileNotFoundError as e:
            print(f"Error: File not found: {e.filename}")
            return []
        except Exception as e:
            print(f"Error: {e}")
            return []

        final_processed_list = []
        for key, movie_data in unified_data.items():
            try:
                domestic = movie_data.get('domestic_box_office_gross', 0)
                international = movie_data.get('international_box_office_gross', 0)
                movie_data['total_box_office_gross'] = domestic + international
                final_processed_list.append(movie_data)
            except Exception as e:
                 print(f"Error {key}: {e}")

        return final_processed_list        