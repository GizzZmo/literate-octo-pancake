#!/usr/bin/env python3
"""
Omni-Grid Data Fetcher
Fetches data from the omni-grid API endpoint
"""

import requests
import json
from typing import Dict, List, Optional, Any
import time


class OmniGridFetcher:
    """Fetches data from the Omni-Grid API"""
    
    def __init__(self, base_url: str = "https://omni-grid-2-0-architect-256533412071.us-west1.run.app"):
        """
        Initialize the fetcher with the base URL
        
        Args:
            base_url: The base URL of the omni-grid API
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'OmniGrid-Analytics-Tool/1.0'
        })
    
    def fetch_data(self, endpoint: str = "", params: Optional[Dict] = None, timeout: int = 30) -> Optional[Dict]:
        """
        Fetch data from the omni-grid API
        
        Args:
            endpoint: API endpoint (default: root)
            params: Query parameters
            timeout: Request timeout in seconds
            
        Returns:
            JSON response data or None if error
        """
        url = f"{self.base_url}/{endpoint}".rstrip('/')
        
        try:
            response = self.session.get(url, params=params, timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
    
    def fetch_grid_data(self) -> Optional[List[Dict]]:
        """
        Fetch grid data from the API
        
        Returns:
            List of grid data items or None if error
        """
        data = self.fetch_data("grid")
        if data and isinstance(data, list):
            return data
        elif data and isinstance(data, dict):
            # If response is a dict, try to extract data array
            return data.get('data', [data])
        return None
    
    def fetch_metrics(self) -> Optional[Dict]:
        """
        Fetch metrics data from the API
        
        Returns:
            Metrics data or None if error
        """
        return self.fetch_data("metrics")
    
    def health_check(self) -> bool:
        """
        Check if the API is accessible
        
        Returns:
            True if API is accessible, False otherwise
        """
        try:
            response = self.session.get(self.base_url, timeout=5)
            return response.status_code == 200
        except:
            return False
