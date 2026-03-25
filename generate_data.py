import pandas as pd
import numpy as np
from datetime import timedelta, date

# Set the random seed for reproducibility
np.random.seed(42)

# Function to create date range

def create_date_range(start_date, num_days):
    return [start_date + timedelta(days=i) for i in range(num_days)]

# Start date
date_start = date(2025, 1, 1)

# Generate dates
dates = create_date_range(date_start, 365)

# Generate data
steps = np.random.normal(loc=8500, scale=2500, size=365)
sleep_hours = np.random.normal(loc=7.2, scale=1.0, size=365)
heart_rate_bpm = np.random.normal(loc=68, scale=10, size=365)
calories_burned = np.random.uniform(1800, 4200, size=365)
active_minutes = np.random.uniform(20, 180, size=365)

# Introduce 5% missing values
for column in [steps, sleep_hours, heart_rate_bpm, calories_burned, active_minutes]:
    indices = np.random.choice(range(365), size=int(0.05*365), replace=False)
    column[indices] = np.nan

# Clip the values to ensure they lie within the specified ranges
steps = np.clip(steps, 3000, 18000)
sleep_hours = np.clip(sleep_hours, 4.5, 9.5)
heart_rate_bpm = np.clip(heart_rate_bpm, 48, 110)

# Create DataFrame
data = pd.DataFrame({
    'Date': dates,
    'Steps': steps,
    'Sleep_Hours': sleep_hours,
    'Heart_Rate_bpm': heart_rate_bpm,
    'Calories_Burned': calories_burned,
    'Active_Minutes': active_minutes
})

# Save to CSV
data.to_csv('data/health_data.csv', index=False)