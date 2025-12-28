# Quick Start Guide - Omni-Grid Analytics Tool

## Installation

```bash
# Clone the repository
git clone https://github.com/GizzZmo/literate-octo-pancake.git
cd literate-octo-pancake

# Install dependencies
pip install -r requirements.txt
```

## Running the Tool

### Option 1: Complete Analysis (Recommended for First Time)

```bash
python omni_analytics.py
```

This will:
- Generate 100 sample records (using mock data since API may not be accessible)
- Perform comprehensive statistical analysis
- Create 7 different visualizations
- Save an analytics report in JSON format
- Output everything to the `output/` directory

### Option 2: Run Examples

```bash
python example_usage.py
```

This demonstrates:
- Basic usage patterns
- Custom analytics queries
- Creating specific visualizations
- Data filtering and aggregation
- Quality checks and correlations

## Understanding the Output

After running the tool, check the `output/` directory for:

### Visualizations (PNG files)
- **category_distribution.png** - Bar chart showing total values by category
- **region_distribution.png** - Pie chart of regional breakdown
- **value_by_status.png** - Box plots showing value ranges for each status
- **value_vs_score.png** - Scatter plot with color-coded categories
- **value_histogram.png** - Frequency distribution of values
- **correlation_heatmap.png** - Shows relationships between numerical features

### Interactive Dashboard
- **interactive_dashboard.html** - Open in your browser for interactive exploration

### Data Report
- **analytics_report.json** - Complete statistical summary in JSON format

## Key Features at a Glance

### Data Analytics
```python
from analytics import DataAnalytics

analytics = DataAnalytics(data)

# Summary statistics
stats = analytics.get_summary_statistics()

# Top performers
top_10 = analytics.get_top_n('value', n=10)

# Aggregations
totals_by_region = analytics.aggregate_by_category('region', 'revenue', 'sum')

# Correlations
corr_matrix = analytics.get_correlation_matrix()
```

### Custom Visualizations
```python
from visualizations import DataVisualizer

viz = DataVisualizer(output_dir="my_charts")

# Create charts
viz.create_bar_chart(data_dict, "My Title", filename="my_chart.png")
viz.create_scatter_plot(data_list, 'x_col', 'y_col', filename="scatter.png")
viz.create_interactive_dashboard(data_list, filename="dashboard.html")
```

### Data Fetching (when API is available)
```python
from data_fetcher import OmniGridFetcher

fetcher = OmniGridFetcher()

# Check health
if fetcher.health_check():
    data = fetcher.fetch_grid_data()
else:
    # Use mock data
    from mock_data import MockDataGenerator
    data = MockDataGenerator().generate_grid_data(100)
```

## Common Use Cases

### 1. Analyze specific categories
```python
analytics = DataAnalytics(data)
filtered = analytics.filter_data({'category': ['A', 'B']})
# Work with filtered data
```

### 2. Find top performers
```python
top_by_value = analytics.get_top_n('value', n=5)
top_by_efficiency = analytics.get_top_n('efficiency', n=5)
```

### 3. Regional analysis
```python
by_region = analytics.aggregate_by_category('region', 'revenue', 'sum')
# Returns: {'North': 123.45, 'South': 234.56, ...}
```

### 4. Data quality checks
```python
quality = analytics.get_data_quality_report()
print(f"Total records: {quality['total_rows']}")
print(f"Missing values: {quality['missing_values']}")
print(f"Duplicates: {quality['duplicate_rows']}")
```

## Troubleshooting

**Problem**: `ModuleNotFoundError` when running scripts  
**Solution**: Make sure you've installed dependencies: `pip install -r requirements.txt`

**Problem**: API not accessible  
**Solution**: The tool automatically falls back to mock data. This is expected in most environments.

**Problem**: No visualizations generated  
**Solution**: Check that matplotlib, seaborn, and plotly are installed. Check the console for error messages.

**Problem**: Output directory not found  
**Solution**: The tool creates it automatically. If you deleted it, it will be recreated on next run.

## Next Steps

- Modify `mock_data.py` to generate data matching your specific use case
- Customize visualizations in `visualizations.py` for your brand colors/style
- Extend `analytics.py` with domain-specific calculations
- Update `data_fetcher.py` when the omni-grid API becomes accessible

## Support

For issues or questions, please open an issue on the GitHub repository.
