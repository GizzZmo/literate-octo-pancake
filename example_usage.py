#!/usr/bin/env python3
"""
Example usage of the Omni-Grid Analytics Tool
Demonstrates various ways to use the tool
"""

from omni_analytics import OmniGridAnalyticsTool
from analytics import DataAnalytics
from visualizations import DataVisualizer
from mock_data import MockDataGenerator

print("=" * 70)
print("OMNI-GRID ANALYTICS TOOL - EXAMPLE USAGE")
print("=" * 70)

# Example 1: Quick Start - Run complete analysis
print("\n### Example 1: Complete Analysis (Quick Start) ###\n")
print("Running full analysis with default settings...")
tool = OmniGridAnalyticsTool(use_mock_data=True)
tool.run_complete_analysis()

# Example 2: Custom Analytics
print("\n" + "=" * 70)
print("### Example 2: Custom Analytics ###\n")

generator = MockDataGenerator(seed=123)
data = generator.generate_grid_data(num_rows=50)

analytics = DataAnalytics(data)

# Get specific insights
print("Top 3 records by value:")
top_3 = analytics.get_top_n('value', n=3)
for i, record in enumerate(top_3, 1):
    print(f"  {i}. ID {record['id']}: ${record['value']:.2f} - {record['category']}")

print("\nValue percentiles:")
percentiles = analytics.get_percentiles('value', [25, 50, 75, 90])
for p, val in percentiles.items():
    print(f"  {p}: ${val:.2f}")

print("\nRevenue by region:")
revenue_by_region = analytics.aggregate_by_category('region', 'revenue', 'sum')
for region, revenue in sorted(revenue_by_region.items(), key=lambda x: x[1], reverse=True):
    print(f"  {region}: ${revenue:,.2f}")

# Example 3: Custom Visualizations
print("\n" + "=" * 70)
print("### Example 3: Custom Visualizations ###\n")

visualizer = DataVisualizer(output_dir="output")

# Filter data and create custom chart
high_value = analytics.filter_data({'category': ['A', 'B']})
print(f"Creating custom visualization for {len(high_value)} filtered records...")

if len(high_value) > 0:
    filepath = visualizer.create_scatter_plot(
        high_value,
        'cost',
        'revenue',
        'category',
        "Cost vs Revenue for Categories A & B",
        "custom_cost_revenue.png"
    )
    print(f"✓ Custom scatter plot saved to {filepath}")

# Example 4: Data Quality Check
print("\n" + "=" * 70)
print("### Example 4: Data Quality Report ###\n")

quality = analytics.get_data_quality_report()
print(f"Total records: {quality['total_rows']}")
print(f"Total fields: {quality['total_columns']}")
print(f"Duplicates: {quality['duplicate_rows']}")
print(f"\nMissing values by field:")
for field, missing in quality['missing_values'].items():
    if missing > 0:
        print(f"  {field}: {missing}")
if sum(quality['missing_values'].values()) == 0:
    print("  No missing values detected ✓")

# Example 5: Correlation Analysis
print("\n" + "=" * 70)
print("### Example 5: Correlation Analysis ###\n")

corr_matrix = analytics.get_correlation_matrix()
if corr_matrix is not None:
    print("Strongest correlations with 'value':")
    value_corr = corr_matrix['value'].sort_values(ascending=False)
    for col, corr in value_corr.items():
        if col != 'value' and abs(corr) > 0.1:
            print(f"  {col}: {corr:.3f}")

print("\n" + "=" * 70)
print("Examples complete! Check the 'output/' directory for all visualizations.")
print("=" * 70)
