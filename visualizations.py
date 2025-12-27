#!/usr/bin/env python3
"""
Visualization Module
Creates various types of visualizations for omni-grid data
"""

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional
import os


class DataVisualizer:
    """Creates visualizations for omni-grid data"""
    
    def __init__(self, output_dir: str = "output"):
        """
        Initialize visualizer
        
        Args:
            output_dir: Directory to save visualizations
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Set style
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 6)
    
    def create_bar_chart(self, data: Dict[str, float], title: str, 
                        xlabel: str = "Category", ylabel: str = "Value",
                        filename: str = "bar_chart.png") -> str:
        """
        Create a bar chart
        
        Args:
            data: Dictionary of category: value pairs
            title: Chart title
            xlabel: X-axis label
            ylabel: Y-axis label
            filename: Output filename
            
        Returns:
            Path to saved chart
        """
        plt.figure(figsize=(12, 6))
        categories = list(data.keys())
        values = list(data.values())
        
        plt.bar(categories, values, color='steelblue', alpha=0.8)
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_pie_chart(self, data: Dict[str, float], title: str,
                        filename: str = "pie_chart.png") -> str:
        """
        Create a pie chart
        
        Args:
            data: Dictionary of category: value pairs
            title: Chart title
            filename: Output filename
            
        Returns:
            Path to saved chart
        """
        plt.figure(figsize=(10, 8))
        labels = list(data.keys())
        values = list(data.values())
        
        colors = sns.color_palette("husl", len(labels))
        plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        plt.title(title, fontsize=16, fontweight='bold')
        plt.axis('equal')
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_line_chart(self, data: List[Dict[str, Any]], x_col: str, y_col: str,
                         title: str, filename: str = "line_chart.png") -> str:
        """
        Create a line chart
        
        Args:
            data: List of data dictionaries
            x_col: Column for x-axis
            y_col: Column for y-axis
            title: Chart title
            filename: Output filename
            
        Returns:
            Path to saved chart
        """
        df = pd.DataFrame(data)
        
        plt.figure(figsize=(14, 6))
        plt.plot(df[x_col], df[y_col], marker='o', linewidth=2, markersize=6, color='steelblue')
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(x_col, fontsize=12)
        plt.ylabel(y_col, fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_heatmap(self, correlation_matrix: pd.DataFrame, title: str,
                      filename: str = "heatmap.png") -> str:
        """
        Create a correlation heatmap
        
        Args:
            correlation_matrix: Correlation matrix DataFrame
            title: Chart title
            filename: Output filename
            
        Returns:
            Path to saved chart
        """
        plt.figure(figsize=(12, 10))
        sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm',
                   center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
        plt.title(title, fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_scatter_plot(self, data: List[Dict[str, Any]], x_col: str, y_col: str,
                           color_col: Optional[str] = None, title: str = "Scatter Plot",
                           filename: str = "scatter_plot.png") -> str:
        """
        Create a scatter plot
        
        Args:
            data: List of data dictionaries
            x_col: Column for x-axis
            y_col: Column for y-axis
            color_col: Optional column for color coding
            title: Chart title
            filename: Output filename
            
        Returns:
            Path to saved chart
        """
        df = pd.DataFrame(data)
        
        plt.figure(figsize=(12, 8))
        if color_col and color_col in df.columns:
            categories = df[color_col].unique()
            colors = sns.color_palette("husl", len(categories))
            for i, cat in enumerate(categories):
                mask = df[color_col] == cat
                plt.scatter(df[mask][x_col], df[mask][y_col], 
                          label=cat, alpha=0.6, s=100, color=colors[i])
            plt.legend()
        else:
            plt.scatter(df[x_col], df[y_col], alpha=0.6, s=100, color='steelblue')
        
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(x_col, fontsize=12)
        plt.ylabel(y_col, fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_histogram(self, data: List[float], title: str, xlabel: str,
                        bins: int = 30, filename: str = "histogram.png") -> str:
        """
        Create a histogram
        
        Args:
            data: List of values
            title: Chart title
            xlabel: X-axis label
            bins: Number of bins
            filename: Output filename
            
        Returns:
            Path to saved chart
        """
        plt.figure(figsize=(12, 6))
        plt.hist(data, bins=bins, color='steelblue', alpha=0.7, edgecolor='black')
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.grid(True, alpha=0.3, axis='y')
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_box_plot(self, data: List[Dict[str, Any]], category_col: str, 
                       value_col: str, title: str,
                       filename: str = "box_plot.png") -> str:
        """
        Create a box plot
        
        Args:
            data: List of data dictionaries
            category_col: Column for categories
            value_col: Column for values
            title: Chart title
            filename: Output filename
            
        Returns:
            Path to saved chart
        """
        df = pd.DataFrame(data)
        
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df, x=category_col, y=value_col, palette="Set2")
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(category_col, fontsize=12)
        plt.ylabel(value_col, fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def create_interactive_dashboard(self, data: List[Dict[str, Any]], 
                                    filename: str = "dashboard.html") -> str:
        """
        Create an interactive Plotly dashboard
        
        Args:
            data: List of data dictionaries
            filename: Output HTML filename
            
        Returns:
            Path to saved dashboard
        """
        df = pd.DataFrame(data)
        
        # Create subplots
        from plotly.subplots import make_subplots
        
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Value Distribution', 'Category vs Value', 
                          'Score Distribution', 'Region Analysis'),
            specs=[[{"type": "histogram"}, {"type": "bar"}],
                   [{"type": "box"}, {"type": "pie"}]]
        )
        
        # Histogram
        if 'value' in df.columns:
            fig.add_trace(
                go.Histogram(x=df['value'], name='Value', marker_color='steelblue'),
                row=1, col=1
            )
        
        # Bar chart
        if 'category' in df.columns and 'value' in df.columns:
            category_sum = df.groupby('category')['value'].sum()
            fig.add_trace(
                go.Bar(x=category_sum.index, y=category_sum.values, 
                      name='Category', marker_color='coral'),
                row=1, col=2
            )
        
        # Box plot
        if 'category' in df.columns and 'score' in df.columns:
            for cat in df['category'].unique():
                cat_data = df[df['category'] == cat]
                fig.add_trace(
                    go.Box(y=cat_data['score'], name=cat),
                    row=2, col=1
                )
        
        # Pie chart
        if 'region' in df.columns:
            region_counts = df['region'].value_counts()
            fig.add_trace(
                go.Pie(labels=region_counts.index, values=region_counts.values),
                row=2, col=2
            )
        
        fig.update_layout(height=800, showlegend=True, title_text="Omni-Grid Data Dashboard")
        
        filepath = os.path.join(self.output_dir, filename)
        fig.write_html(filepath)
        
        return filepath
