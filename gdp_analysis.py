import streamlit as st
import pandas as pd
import plotly.express as px


# Set page config
st.set_page_config(
    page_title="GDP Analysis App",
    layout="wide"
)
# Load GDP data
@st.cache_data
def load_data():
    df = pd.read_csv('gdp.csv')  # Replace 'your_data.csv' with the actual file name
    return df

df = load_data()
# Sidebar - Navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('', ['GDP Growth of a country','GDP Value Comparison between countries', 'GDP Growth Comparison worldwide','GDP Trends worldwide', 'Top GDP Performers'],label_visibility = 'collapsed')

# Page title
st.title('Global GDP Analysis from 1960 - 2016')

# GDP Growth Analysis Page
if page == 'GDP Growth of a country':
    st.header('Growth Rate of a country')

    # Sidebar - Country selection for single country GDP growth
    selected_country_growth = st.sidebar.selectbox('', df['Country Name'].unique(), label_visibility='collapsed')


    if selected_country_growth:
        st.subheader(f'GDP Growth of {selected_country_growth}')
        country_data = df[df['Country Name'] == selected_country_growth]
        
        # Calculate GDP growth rate
        country_data['Growth Rate'] = country_data['Value'].pct_change() * 100
        
        # Plot GDP growth
        st.line_chart(country_data.set_index('Year')['Growth Rate'])

        # Show raw GDP growth data
        st.subheader(f'Raw GDP Growth Data for {selected_country_growth}')
        st.write(country_data)  # Display all columns
# GDP Comparison Page
elif page == 'GDP Value Comparison between countries':
    st.header('GDP Comparison')

    # Sidebar - Country selection for GDP comparison
    selected_countries_comparison = st.sidebar.multiselect('Select countries:', df['Country Name'].unique(), label_visibility='collapsed')

    if selected_countries_comparison:
        st.subheader('GDP Comparison Across Selected Countries')
        comparison_data = df[df['Country Name'].isin(selected_countries_comparison)]
        
        # Plot GDP comparison using Plotly
        fig = px.line(comparison_data, x='Year', y='Value', color='Country Name', title='GDP Comparison Across Selected Countries')
        st.plotly_chart(fig)

# GDP Growth Rate Comparison Page
elif page == 'GDP Growth Comparison worldwide':
    st.header('GDP Growth Rate Comparison worldwide')

    # Calculate GDP growth rates for each country
    df['GDP Growth Rate'] = df.groupby('Country Name')['Value'].pct_change() * 100

    # Plot GDP growth rate comparison using Plotly
    fig = px.line(df, x='Year', y='GDP Growth Rate', color='Country Name', title='GDP Growth Rate Comparison')
    st.plotly_chart(fig)
# GDP Trends Page
elif page == 'GDP Trends worldwide':
    st.header('GDP Trends Over Time')

    # Plot overall GDP trends using Plotly
    fig = px.line(df, x='Year', y='Value', color='Country Name', title='GDP Trends Over Time')
    st.plotly_chart(fig)

# Top GDP Performers Page
elif page == 'Top GDP Performers':
    st.header('Top GDP Performers')

    # Calculate total GDP for each country
    top_countries = df.groupby('Country Name')['Value'].sum().sort_values(ascending=False).head(10)

    # Plot top GDP performers using Plotly
    fig = px.bar(top_countries, x=top_countries.index, y=top_countries.values, title='Top GDP Performers')
    fig.update_layout(xaxis_title='Country', yaxis_title='Total GDP')
    st.plotly_chart(fig)
