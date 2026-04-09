import pandas as pd


def load_data():
    """
    Load and clean the health data from a CSV file.

    Returns:
        pd.DataFrame: A pandas DataFrame with cleaned data.
    """
    # Load the data from the CSV file
    file_path = 'data/health_data.csv'
    data = pd.read_csv(file_path)

    # Fill missing 'Steps' values with median of the 'Steps' column
    data['Steps'] = data['Steps'].fillna(data['Steps'].median())

    # Fill missing 'Sleep_Hours' values with 7.0 (assumed average sleep time)
    data['Sleep_Hours'] = data['Sleep_Hours'].fillna(7.0)

    # Fill missing 'Heart_Rate_bpm' with 68 (assumed average resting heart rate)
    data['Heart_Rate_bpm'] = data['Heart_Rate_bpm'].fillna(68)

    # Fill other columns with their respective median values
    for column in data.columns:
        if data[column].isnull().any():
            data[column] = data[column].fillna(data[column].median())

    # Convert 'Date' column to datetime objects
    data['Date'] = pd.to_datetime(data['Date'])

    return data

def calculate_recovery_score(df):
    """
    Calculate and add a 'Recovery_Score' column to the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing health data.

    Returns:
        pd.DataFrame: The DataFrame with an added 'Recovery_Score' column.
    """
    def clamp(n, minn, maxn):
        return max(min(maxn, n), minn)

    recovery_scores = []

    for index, row in df.iterrows():
        score = 50  # Start with a base score of 50

        # Adjust score based on Sleep_Hours
        if row['Sleep_Hours'] >= 7:
            score += 20  # good sleep adds to the score
        elif row['Sleep_Hours'] < 6:
            score -= 20  # poor sleep deducts from the score
        else:
            score += 10  # average sleep adds slightly to the score

        # Adjust score based on Heart_Rate_bpm (lower is better)
        heart_rate_score = 68 - row['Heart_Rate_bpm']
        score += heart_rate_score  # low heart rate adds to recovery

        # Adjust score based on Steps
        if row['Steps'] > 14000:
            score -= 10  # very high activity reduces recovery due to strain
        elif row['Steps'] < 4000:
            score -= 10  # very low activity might indicate poor recovery

        # Ensure the score is clamped between 0 and 100
        score = clamp(score, 0, 100)
        recovery_scores.append(score)

    df['Recovery_Score'] = recovery_scores
    return df


def process_data():
    """
    Main function to load and process health data for the dashboard.

    Returns:
        pd.DataFrame: The final processed DataFrame with Recovery Score.
    """
    # Load cleaned data
    df = load_data()

    # Add Recovery Score
    df = calculate_recovery_score(df)

    return df

