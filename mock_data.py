#!/usr/bin/env python3
"""
Mock Data Generator for Omni-Grid
Generates sample data for testing when the API is not available
"""

import random
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Any


class MockDataGenerator:
    """Generates mock omni-grid data for testing"""
    
    def __init__(self, seed: int = 42):
        """Initialize with a random seed for reproducibility"""
        random.seed(seed)
        np.random.seed(seed)
    
    def generate_grid_data(self, num_rows: int = 100) -> List[Dict[str, Any]]:
        """
        Generate mock grid data
        
        Args:
            num_rows: Number of data rows to generate
            
        Returns:
            List of grid data dictionaries
        """
        data = []
        categories = ['A', 'B', 'C', 'D', 'E']
        regions = ['North', 'South', 'East', 'West', 'Central']
        statuses = ['Active', 'Inactive', 'Pending', 'Completed']
        
        base_date = datetime.now() - timedelta(days=365)
        
        for i in range(num_rows):
            row = {
                'id': i + 1,
                'category': random.choice(categories),
                'region': random.choice(regions),
                'status': random.choice(statuses),
                'value': round(random.uniform(10, 1000), 2),
                'quantity': random.randint(1, 100),
                'score': round(random.uniform(0, 100), 2),
                'timestamp': (base_date + timedelta(days=random.randint(0, 365))).isoformat(),
                'priority': random.choice(['High', 'Medium', 'Low']),
                'efficiency': round(random.uniform(0.5, 1.0), 3),
                'cost': round(random.uniform(100, 5000), 2),
                'revenue': round(random.uniform(150, 6000), 2)
            }
            data.append(row)
        
        return data
    
    def generate_metrics(self) -> Dict[str, Any]:
        """
        Generate mock metrics data
        
        Returns:
            Dictionary of metrics
        """
        return {
            'total_records': random.randint(1000, 10000),
            'active_users': random.randint(50, 500),
            'avg_response_time': round(random.uniform(0.1, 2.0), 3),
            'success_rate': round(random.uniform(0.85, 0.99), 4),
            'uptime': round(random.uniform(0.95, 0.999), 5),
            'last_updated': datetime.now().isoformat()
        }
    
    def generate_time_series(self, num_points: int = 50) -> List[Dict[str, Any]]:
        """
        Generate mock time series data
        
        Args:
            num_points: Number of time points to generate
            
        Returns:
            List of time series data points
        """
        data = []
        base_date = datetime.now() - timedelta(days=num_points)
        base_value = 100
        
        for i in range(num_points):
            # Add trend and noise
            trend = i * 0.5
            noise = random.gauss(0, 10)
            value = base_value + trend + noise
            
            data.append({
                'date': (base_date + timedelta(days=i)).strftime('%Y-%m-%d'),
                'value': round(max(0, value), 2),
                'moving_avg': round(max(0, base_value + trend), 2)
            })
        
        return data
