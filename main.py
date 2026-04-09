import pandas as pd   # Ensure pandas is imported as we use it for date filtering
import streamlit as st
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
    df = sidebar_filters(df)
    
    # Calculate metrics from filtered data
    average_steps = df['Steps'].mean()
    average_sleep_hours = df['Sleep_Hours'].mean()
    average_recovery_score = df['Recovery_Score'].mean()

    # Create a 3-column layout to display metrics
    col1, col2, col3 = st.columns(3)

    # Display metrics in each column
    with col1:
        st.metric(label="Average Steps", value=f"{average_steps:.0f}", delta=None)

    with col2:
        st.metric(label="Average Sleep Hours", value=f"{average_sleep_hours:.1f}", delta=None)

    with col3:
        st.metric(label="Average Recovery Score", value=f"{average_recovery_score:.1f}", delta=None)

    # Placeholder for future interactive components or data visualization
    st.header("Dashboard Overview")

    # Display initial data metrics or summaries
    st.write("### Data Preview")
    st.dataframe(df.head())

if __name__ == "__main__":
    main()
