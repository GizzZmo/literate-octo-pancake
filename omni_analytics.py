#!/usr/bin/env python3
"""
Omni-Grid Data Analytics Tool
Main application for fetching, analyzing, and visualizing omni-grid data
"""

import sys
import json
from typing import Optional
from data_fetcher import OmniGridFetcher
from mock_data import MockDataGenerator
from analytics import DataAnalytics
from visualizations import DataVisualizer


class OmniGridAnalyticsTool:
    """Main analytics tool orchestrator"""
    
    def __init__(self, use_mock_data: bool = False):
        """
        Initialize the analytics tool
        
        Args:
            use_mock_data: If True, use mock data instead of fetching from API
        """
        self.use_mock_data = use_mock_data
        self.fetcher = OmniGridFetcher()
        self.mock_generator = MockDataGenerator()
        self.visualizer = DataVisualizer()
        self.data = None
        self.analytics = None
    
    def load_data(self, num_records: int = 100) -> bool:
        """
        Load data from API or mock generator
        
        Args:
            num_records: Number of records to generate if using mock data
            
        Returns:
            True if data loaded successfully
        """
        print("=" * 60)
        print("LOADING DATA")
        print("=" * 60)
        
        if self.use_mock_data:
            print("Using mock data generator...")
            self.data = self.mock_generator.generate_grid_data(num_records)
            print(f"✓ Generated {len(self.data)} mock records")
        else:
            print("Attempting to fetch data from omni-grid API...")
            if not self.fetcher.health_check():
                print("✗ API not accessible, falling back to mock data")
                self.data = self.mock_generator.generate_grid_data(num_records)
                print(f"✓ Generated {len(self.data)} mock records")
            else:
                self.data = self.fetcher.fetch_grid_data()
                if self.data:
                    print(f"✓ Fetched {len(self.data)} records from API")
                else:
                    print("✗ Failed to fetch data, using mock data")
                    self.data = self.mock_generator.generate_grid_data(num_records)
                    print(f"✓ Generated {len(self.data)} mock records")
        
        if self.data:
            self.analytics = DataAnalytics(self.data)
            return True
        return False
    
    def display_data_overview(self):
        """Display overview of the loaded data"""
        print("\n" + "=" * 60)
        print("DATA OVERVIEW")
        print("=" * 60)
        
        if not self.data:
            print("✗ No data loaded")
            return
        
        print(f"Total Records: {len(self.data)}")
        if self.data:
            print(f"Columns: {', '.join(self.data[0].keys())}")
            print(f"\nFirst 3 records:")
            for i, record in enumerate(self.data[:3], 1):
                print(f"\n  Record {i}:")
                for key, value in record.items():
                    print(f"    {key}: {value}")
    
    def run_analytics(self):
        """Run various analytics on the data"""
        print("\n" + "=" * 60)
        print("ANALYTICS RESULTS")
        print("=" * 60)
        
        if not self.analytics:
            print("✗ No analytics engine initialized")
            return
        
        # Summary statistics
        print("\n1. SUMMARY STATISTICS")
        print("-" * 60)
        summary = self.analytics.get_summary_statistics()
        for col, stats in summary.items():
            print(f"\n{col.upper()}:")
            print(f"  Mean:   {stats['mean']:.2f}")
            print(f"  Median: {stats['median']:.2f}")
            print(f"  Std:    {stats['std']:.2f}")
            print(f"  Min:    {stats['min']:.2f}")
            print(f"  Max:    {stats['max']:.2f}")
        
        # Categorical distributions
        print("\n2. CATEGORICAL DISTRIBUTIONS")
        print("-" * 60)
        for col in ['category', 'region', 'status']:
            if col in self.analytics.df.columns:
                dist = self.analytics.get_categorical_distribution(col)
                print(f"\n{col.upper()} Distribution:")
                for key, count in sorted(dist.items(), key=lambda x: x[1], reverse=True):
                    print(f"  {key}: {count}")
        
        # Data quality
        print("\n3. DATA QUALITY REPORT")
        print("-" * 60)
        quality = self.analytics.get_data_quality_report()
        print(f"Total Rows: {quality['total_rows']}")
        print(f"Total Columns: {quality['total_columns']}")
        print(f"Duplicate Rows: {quality['duplicate_rows']}")
        
        # Top performers
        print("\n4. TOP 5 BY VALUE")
        print("-" * 60)
        if 'value' in self.analytics.df.columns:
            top_records = self.analytics.get_top_n('value', n=5)
            for i, record in enumerate(top_records, 1):
                print(f"\n  {i}. ID: {record.get('id')}, Value: {record.get('value')}, "
                      f"Category: {record.get('category')}, Region: {record.get('region')}")
    
    def generate_visualizations(self):
        """Generate all visualizations"""
        print("\n" + "=" * 60)
        print("GENERATING VISUALIZATIONS")
        print("=" * 60)
        
        if not self.data or not self.analytics:
            print("✗ No data available for visualization")
            return
        
        generated_files = []
        
        # 1. Bar chart - Category distribution
        print("\n1. Creating category distribution bar chart...")
        if 'category' in self.analytics.df.columns and 'value' in self.analytics.df.columns:
            category_data = self.analytics.aggregate_by_category('category', 'value', 'sum')
            filepath = self.visualizer.create_bar_chart(
                category_data,
                "Total Value by Category",
                "Category",
                "Total Value",
                "category_distribution.png"
            )
            generated_files.append(filepath)
            print(f"   ✓ Saved to {filepath}")
        
        # 2. Pie chart - Region distribution
        print("\n2. Creating region distribution pie chart...")
        if 'region' in self.analytics.df.columns:
            region_dist = self.analytics.get_categorical_distribution('region')
            filepath = self.visualizer.create_pie_chart(
                region_dist,
                "Distribution by Region",
                "region_distribution.png"
            )
            generated_files.append(filepath)
            print(f"   ✓ Saved to {filepath}")
        
        # 3. Box plot - Value by status
        print("\n3. Creating box plot for value by status...")
        if 'status' in self.analytics.df.columns and 'value' in self.analytics.df.columns:
            filepath = self.visualizer.create_box_plot(
                self.data,
                'status',
                'value',
                "Value Distribution by Status",
                "value_by_status.png"
            )
            generated_files.append(filepath)
            print(f"   ✓ Saved to {filepath}")
        
        # 4. Scatter plot - Value vs Score
        print("\n4. Creating scatter plot for value vs score...")
        if 'value' in self.analytics.df.columns and 'score' in self.analytics.df.columns:
            filepath = self.visualizer.create_scatter_plot(
                self.data,
                'value',
                'score',
                'category',
                "Value vs Score by Category",
                "value_vs_score.png"
            )
            generated_files.append(filepath)
            print(f"   ✓ Saved to {filepath}")
        
        # 5. Histogram - Value distribution
        print("\n5. Creating histogram for value distribution...")
        if 'value' in self.analytics.df.columns:
            values = self.analytics.df['value'].tolist()
            filepath = self.visualizer.create_histogram(
                values,
                "Value Distribution",
                "Value",
                30,
                "value_histogram.png"
            )
            generated_files.append(filepath)
            print(f"   ✓ Saved to {filepath}")
        
        # 6. Correlation heatmap
        print("\n6. Creating correlation heatmap...")
        corr_matrix = self.analytics.get_correlation_matrix()
        if corr_matrix is not None and not corr_matrix.empty:
            filepath = self.visualizer.create_heatmap(
                corr_matrix,
                "Correlation Matrix",
                "correlation_heatmap.png"
            )
            generated_files.append(filepath)
            print(f"   ✓ Saved to {filepath}")
        
        # 7. Interactive dashboard
        print("\n7. Creating interactive dashboard...")
        filepath = self.visualizer.create_interactive_dashboard(
            self.data,
            "interactive_dashboard.html"
        )
        generated_files.append(filepath)
        print(f"   ✓ Saved to {filepath}")
        
        return generated_files
    
    def save_analytics_report(self, filename: str = "output/analytics_report.json"):
        """Save analytics results to JSON file"""
        if not self.analytics:
            return None
        
        report = {
            "summary_statistics": self.analytics.get_summary_statistics(),
            "data_quality": self.analytics.get_data_quality_report(),
            "categorical_distributions": {}
        }
        
        for col in ['category', 'region', 'status']:
            if col in self.analytics.df.columns:
                report["categorical_distributions"][col] = \
                    self.analytics.get_categorical_distribution(col)
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        return filename
    
    def run_complete_analysis(self):
        """Run complete analysis workflow"""
        print("\n" + "=" * 60)
        print("OMNI-GRID DATA ANALYTICS TOOL")
        print("=" * 60)
        
        # Load data
        if not self.load_data():
            print("\n✗ Failed to load data. Exiting.")
            return False
        
        # Display overview
        self.display_data_overview()
        
        # Run analytics
        self.run_analytics()
        
        # Generate visualizations
        files = self.generate_visualizations()
        
        # Save report
        print("\n" + "=" * 60)
        print("SAVING REPORT")
        print("=" * 60)
        report_file = self.save_analytics_report()
        if report_file:
            print(f"✓ Analytics report saved to {report_file}")
        
        # Summary
        print("\n" + "=" * 60)
        print("ANALYSIS COMPLETE")
        print("=" * 60)
        print(f"✓ Analyzed {len(self.data)} records")
        print(f"✓ Generated {len(files)} visualizations")
        print(f"✓ All outputs saved to 'output/' directory")
        print("\nGenerated files:")
        for f in files:
            print(f"  - {f}")
        if report_file:
            print(f"  - {report_file}")
        
        return True


def main():
    """Main entry point"""
    # Use mock data by default (set to False to try API first)
    tool = OmniGridAnalyticsTool(use_mock_data=True)
    
    try:
        success = tool.run_complete_analysis()
        return 0 if success else 1
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
