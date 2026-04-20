import pandas as pd   # Ensure pandas is imported as we use it for date filtering
import streamlit as st
import plotly.express as px
from modules.processor import process_data
# Sidebar for filtering
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
    # Load and process the data
    df = process_data()
    
    # Apply sidebar filters
    filtered_df = sidebar_filters(df)
    
    # Calculate metrics from filtered data
    average_steps = filtered_df['Steps'].mean()
    average_sleep_hours = filtered_df['Sleep_Hours'].mean()
    average_recovery_score = filtered_df['Recovery_Score'].mean()

    # Create a 3-column layout to display metrics
    col1, col2, col3 = st.columns(3)

    # Display metrics in each column
    with col1:
        st.metric(label="Average Steps", value=f"{average_steps:.0f}", delta=None)

    with col2:
        st.metric(label="Average Sleep Hours", value=f"{average_sleep_hours:.1f}", delta=None)

    with col3:
        st.metric(label="Average Recovery Score", value=f"{average_recovery_score:.1f}", delta=None)
    
    # Visualization Columns
    first_col, second_col = st.columns(2)
    
    # Left Column: Dual Line Chart
    with first_col:
        st.subheader("Recovery Score & Sleep Trend")
        fig1 = px.line(filtered_df, x='Date', y=['Recovery_Score', 'Sleep_Hours'], title="Recovery Score & Sleep Trend")
        st.plotly_chart(fig1, use_container_width=True)

    # Right Column: Scatter Plot
    with second_col:
        st.subheader("Recovery Score vs Daily Steps")
        fig2 = px.scatter(filtered_df, x='Steps', y='Recovery_Score', color='Sleep_Hours', title="Recovery Score vs Daily Steps")
        st.plotly_chart(fig2, use_container_width=True)

    # Additional Two Columns for More Plots
    third_col, fourth_col = st.columns(2)
    
    # Left Column: Scatter Plot
    with third_col:
        st.subheader("Recovery Score vs Resting Heart Rate")
        fig3 = px.scatter(filtered_df, x='Heart_Rate_bpm', y='Recovery_Score', title="Recovery Score vs Resting Heart Rate")
        st.plotly_chart(fig3, use_container_width=True)
    
    # Right Column: Line Chart
    with fourth_col:
        st.subheader("Daily Calories Burned Trend")
        fig4 = px.line(filtered_df, x='Date', y='Calories_Burned', title="Daily Calories Burned Trend")
        st.plotly_chart(fig4, use_container_width=True)

if __name__ == "__main__":
    main()
