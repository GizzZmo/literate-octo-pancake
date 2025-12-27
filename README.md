# Omni-Grid Data Analytics Tool

A comprehensive data analytics tool for fetching, analyzing, and visualizing omni-grid data with multiple visualization types.

**Omni-Grid API:** https://omni-grid-2-0-architect-256533412071.us-west1.run.app

## Features

### Data Collection
- **API Integration**: Fetches data from the omni-grid API endpoint
- **Mock Data Generator**: Generates realistic sample data for testing when API is unavailable
- **Flexible Data Loading**: Automatically falls back to mock data if API is inaccessible

### Analytics Capabilities
- **Summary Statistics**: Mean, median, standard deviation, min/max for all numerical columns
- **Categorical Analysis**: Distribution analysis for categorical variables
- **Correlation Analysis**: Correlation matrix for numerical features
- **Data Aggregation**: Group and aggregate data by various dimensions
- **Top-N Analysis**: Identify top performers or outliers
- **Data Quality Reports**: Missing values, duplicates, data types
- **Percentile Calculations**: Customizable percentile analysis

### Visualizations

The tool generates 7 different types of visualizations:

1. **Bar Chart**: Total value by category
2. **Pie Chart**: Distribution by region
3. **Box Plot**: Value distribution by status
4. **Scatter Plot**: Value vs score relationships with category coloring
5. **Histogram**: Value distribution frequency
6. **Heatmap**: Correlation matrix for numerical features
7. **Interactive Dashboard**: Plotly-based interactive HTML dashboard

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/GizzZmo/literate-octo-pancake.git
cd literate-octo-pancake
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start

Run the complete analysis with a single command:

```bash
python omni_analytics.py
```

This will:
1. Load data from the omni-grid API (or use mock data)
2. Perform comprehensive analytics
3. Generate all visualizations
4. Save results to the `output/` directory

### Output

All outputs are saved to the `output/` directory:

- `category_distribution.png` - Bar chart of values by category
- `region_distribution.png` - Pie chart of regional distribution
- `value_by_status.png` - Box plot showing value ranges by status
- `value_vs_score.png` - Scatter plot of value vs score
- `value_histogram.png` - Histogram of value distribution
- `correlation_heatmap.png` - Correlation matrix heatmap
- `interactive_dashboard.html` - Interactive dashboard (open in browser)
- `analytics_report.json` - Complete analytics results in JSON format

### Using as a Library

You can also use the tool programmatically:

```python
from omni_analytics import OmniGridAnalyticsTool

# Initialize tool (use_mock_data=False to try API first)
tool = OmniGridAnalyticsTool(use_mock_data=True)

# Load data
tool.load_data(num_records=100)

# Run analytics
tool.run_analytics()

# Generate visualizations
tool.generate_visualizations()

# Access the analytics engine directly
analytics = tool.analytics
summary = analytics.get_summary_statistics()
correlations = analytics.get_correlation_matrix()
```

### Advanced Usage

#### Custom Data Analysis

```python
from analytics import DataAnalytics
from mock_data import MockDataGenerator

# Generate custom data
generator = MockDataGenerator()
data = generator.generate_grid_data(num_rows=500)

# Analyze
analytics = DataAnalytics(data)

# Get specific insights
top_values = analytics.get_top_n('value', n=10)
category_totals = analytics.aggregate_by_category('category', 'value', 'sum')
percentiles = analytics.get_percentiles('score', [25, 50, 75, 90, 95])
```

#### Custom Visualizations

```python
from visualizations import DataVisualizer
from mock_data import MockDataGenerator

# Setup
generator = MockDataGenerator()
visualizer = DataVisualizer(output_dir="custom_output")

# Generate data
data = generator.generate_grid_data(100)

# Create custom charts
visualizer.create_bar_chart(
    {'A': 100, 'B': 200, 'C': 150},
    title="Custom Bar Chart",
    filename="my_chart.png"
)

visualizer.create_scatter_plot(
    data,
    x_col='value',
    y_col='score',
    color_col='region',
    title="My Scatter Plot",
    filename="my_scatter.png"
)
```

#### Fetching Real API Data

```python
from data_fetcher import OmniGridFetcher

fetcher = OmniGridFetcher()

# Check API health
if fetcher.health_check():
    # Fetch grid data
    data = fetcher.fetch_grid_data()
    
    # Fetch metrics
    metrics = fetcher.fetch_metrics()
else:
    print("API not accessible")
```

## Module Overview

### `data_fetcher.py`
Handles communication with the omni-grid API:
- `OmniGridFetcher`: Main class for API interactions
- Health checks and error handling
- Configurable timeouts and parameters

### `mock_data.py`
Generates realistic sample data:
- `MockDataGenerator`: Creates synthetic omni-grid data
- Reproducible with seed control
- Various data types: grid data, metrics, time series

### `analytics.py`
Core analytics engine:
- `DataAnalytics`: Statistical analysis and data processing
- Summary statistics, aggregations, filtering
- Data quality reporting

### `visualizations.py`
Visualization generation:
- `DataVisualizer`: Creates static and interactive charts
- Multiple chart types with matplotlib, seaborn, and plotly
- Customizable styling and output formats

### `omni_analytics.py`
Main orchestrator:
- `OmniGridAnalyticsTool`: Coordinates all components
- Complete workflow execution
- Report generation

## Data Schema

The tool expects omni-grid data with the following structure:

```json
{
  "id": 1,
  "category": "A",
  "region": "North",
  "status": "Active",
  "value": 523.45,
  "quantity": 42,
  "score": 87.3,
  "timestamp": "2024-03-15T10:30:00",
  "priority": "High",
  "efficiency": 0.892,
  "cost": 1250.00,
  "revenue": 1875.50
}
```

## Requirements

- pandas>=2.1.4
- matplotlib>=3.8.2
- seaborn>=0.13.0
- plotly>=5.18.0
- requests>=2.31.0
- numpy>=1.26.3

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For issues or questions, please open an issue on GitHub.
