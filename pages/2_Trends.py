import pandas as pd
import streamlit as st
import plotly.express as px
from modules.processor import process_data

# Sidebar for filtering (copied from Dashboard page)
def sidebar_filters(df):
    """
    Sidebar filter for time range selection.

    Args:
        df (pd.DataFrame): The DataFrame to filter.

    Returns:
        pd.DataFrame: Filtered DataFrame based on user selection.
    """
    st.sidebar.header("Filters")
    
    # Select box for time range
    time_range = st.sidebar.selectbox(
        "Select Time Range",
        options=["Last 7 Days", "Last 30 Days", "All Time"],
        index=2
    )

    # Filter df based on sidebar selection
    if time_range == "Last 7 Days":
        filtered_df = df[df['Date'] >= df['Date'].max() - pd.Timedelta(days=7)]
    elif time_range == "Last 30 Days":
        filtered_df = df[df['Date'] >= df['Date'].max() - pd.Timedelta(days=30)]
    else:
        filtered_df = df

    return filtered_df

# Main function
def main():
    # Set the title for the page
    st.title("Trends & Insights")
    
    # Load and process the data
    @st.cache_data
    def load_data():
        return process_data()
    
    df = load_data()

    # Apply sidebar filters
    filtered_df = sidebar_filters(df)
    
    # Display summary statistics
    st.subheader("Summary Statistics")
    st.write(filtered_df[['Recovery_Score', 'Sleep_Hours', 'Steps', 'Calories_Burned']].describe().loc[['mean', 'min', 'max']])
    
    # Monthly average line chart for Recovery Score
    st.subheader("Monthly Average Recovery Score")
    filtered_df['Month'] = filtered_df['Date'].dt.to_period('M').dt.to_timestamp()
    monthly_avg_recovery = filtered_df.groupby('Month').Recovery_Score.mean().reset_index()
    fig = px.line(monthly_avg_recovery, x='Month', y='Recovery_Score', title="Average Recovery Score Per Month")
    st.plotly_chart(fig, use_container_width=True)

    # Histograms for distribution analysis
    st.subheader("Distribution of Health Metrics")
    
    # Histogram for Steps
    fig1 = px.histogram(filtered_df, x='Steps', nbins=50, title="Steps Distribution")
    st.plotly_chart(fig1, use_container_width=True)
    
    # Histogram for Calories Burned
    fig2 = px.histogram(filtered_df, x='Calories_Burned', nbins=50, title="Calories Burned Distribution")
    st.plotly_chart(fig2, use_container_width=True)
    
    # Histogram for Recovery Score
    fig3 = px.histogram(filtered_df, x='Recovery_Score', nbins=50, title="Recovery Score Distribution")
    st.plotly_chart(fig3, use_container_width=True)
    
    # Histogram for Sleep Hours
    fig4 = px.histogram(filtered_df, x='Sleep_Hours', nbins=50, title="Sleep Hours Distribution")
    st.plotly_chart(fig4, use_container_width=True)

if __name__ == "__main__":
    main()