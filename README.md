# Global GDP Analysis Web Application

This web application allows users to analyze global Gross Domestic Product (GDP) data from the years 1960 to 2016. It provides various features to explore GDP trends, growth rates, and comparisons between different countries.

## Technologies Used
- **Streamlit**: This is used to create the web application interface.
- **Pandas**: For data manipulation and analysis.
- **Plotly**: For interactive data visualization.

## Data Source
- The GDP data used in this project is sourced from [The World Bank](https://databank.worldbank.org/).

## Features
- **GDP Growth Analysis**: Users can select a specific country to visualize its GDP growth rate over the years. The application calculates the growth rate and displays it in a line chart.
- **GDP Value Comparison**: Users can compare the GDP values of multiple countries over time. They can select countries from a dropdown menu, and the application generates a line chart comparing their GDP values.
- **GDP Growth Rate Comparison**: This feature allows users to compare the GDP growth rates of different countries worldwide. The application calculates the growth rate for each country and visualizes the comparison in a line chart.
- **GDP Trends Over Time**: Users can view the overall GDP trends over the years for multiple countries. The application generates a line chart showing the GDP values of selected countries over time.
- **Top GDP Performers**: Users can see the top GDP performers by total GDP value. The application displays a bar chart showing the total GDP of the top 10 countries.

## How to Run
1. Install Python and the required libraries:
   ```bash
   pip install streamlit pandas plotly
   ```
2. Download the gdp.csv file and save it in the same directory as the Python code.
3. Run the application from the command line:
  ```bash
  streamlit run app.py  # Replace 'app.py' with your actual file name
```

## OUTPUT
#### Users can interact with various visualizations to gain insights into GDP trends and comparisons.
Here's the link : [GDP Analysis](https://global-gdp-analysis-c3cehffc4w2pxaxntfyfc6.streamlit.app/)


