#!/usr/bin/env python3
"""
Data Analytics Engine
Performs various statistical analyses on omni-grid data
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional


class DataAnalytics:
    """Analytics engine for processing and analyzing omni-grid data"""
    
    def __init__(self, data: List[Dict[str, Any]]):
        """
        Initialize with data
        
        Args:
            data: List of dictionaries containing grid data
        """
        self.df = pd.DataFrame(data)
        self.original_data = data
    
    def get_summary_statistics(self) -> Dict[str, Any]:
        """
        Calculate summary statistics for numerical columns
        
        Returns:
            Dictionary of summary statistics
        """
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        summary = {}
        
        for col in numeric_cols:
            summary[col] = {
                'mean': float(self.df[col].mean()),
                'median': float(self.df[col].median()),
                'std': float(self.df[col].std()),
                'min': float(self.df[col].min()),
                'max': float(self.df[col].max()),
                'count': int(self.df[col].count())
            }
        
        return summary
    
    def get_categorical_distribution(self, column: str) -> Dict[str, int]:
        """
        Get distribution of categorical values
        
        Args:
            column: Column name to analyze
            
        Returns:
            Dictionary with value counts
        """
        if column not in self.df.columns:
            return {}
        
        return self.df[column].value_counts().to_dict()
    
    def get_correlation_matrix(self) -> Optional[pd.DataFrame]:
        """
        Calculate correlation matrix for numerical columns
        
        Returns:
            Correlation matrix as DataFrame
        """
        numeric_df = self.df.select_dtypes(include=[np.number])
        if numeric_df.empty:
            return None
        return numeric_df.corr()
    
    def aggregate_by_category(self, category_col: str, value_col: str, 
                             agg_func: str = 'sum') -> Dict[str, float]:
        """
        Aggregate values by category
        
        Args:
            category_col: Column to group by
            value_col: Column to aggregate
            agg_func: Aggregation function ('sum', 'mean', 'count', etc.)
            
        Returns:
            Dictionary with aggregated values
        """
        if category_col not in self.df.columns or value_col not in self.df.columns:
            return {}
        
        result = self.df.groupby(category_col)[value_col].agg(agg_func)
        return result.to_dict()
    
    def get_top_n(self, column: str, n: int = 10, ascending: bool = False) -> List[Dict]:
        """
        Get top N records by a column value
        
        Args:
            column: Column to sort by
            n: Number of records to return
            ascending: Sort order
            
        Returns:
            List of top records
        """
        if column not in self.df.columns:
            return []
        
        top_df = self.df.nlargest(n, column) if not ascending else self.df.nsmallest(n, column)
        return top_df.to_dict('records')
    
    def filter_data(self, conditions: Dict[str, Any]) -> List[Dict]:
        """
        Filter data based on conditions
        
        Args:
            conditions: Dictionary of column: value pairs
            
        Returns:
            Filtered data as list of dictionaries
        """
        filtered_df = self.df.copy()
        
        for col, value in conditions.items():
            if col in filtered_df.columns:
                if isinstance(value, (list, tuple)):
                    filtered_df = filtered_df[filtered_df[col].isin(value)]
                else:
                    filtered_df = filtered_df[filtered_df[col] == value]
        
        return filtered_df.to_dict('records')
    
    def get_percentiles(self, column: str, percentiles: List[float] = None) -> Dict[str, float]:
        """
        Calculate percentiles for a column
        
        Args:
            column: Column name
            percentiles: List of percentiles (0-100)
            
        Returns:
            Dictionary of percentile values
        """
        if percentiles is None:
            percentiles = [25, 50, 75, 90, 95, 99]
        
        if column not in self.df.columns:
            return {}
        
        result = {}
        for p in percentiles:
            result[f'p{p}'] = float(self.df[column].quantile(p / 100))
        
        return result
    
    def get_data_quality_report(self) -> Dict[str, Any]:
        """
        Generate data quality report
        
        Returns:
            Dictionary with data quality metrics
        """
        return {
            'total_rows': len(self.df),
            'total_columns': len(self.df.columns),
            'missing_values': self.df.isnull().sum().to_dict(),
            'duplicate_rows': int(self.df.duplicated().sum()),
            'column_types': {col: str(dtype) for col, dtype in self.df.dtypes.items()}
        }
