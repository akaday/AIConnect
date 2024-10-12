# src/tools/data_fetcher.py
import requests

class DataFetcher:
    @staticmethod
    def fetch_data(api_url, params=None):
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # ensure we notice bad responses
        return response.json()
