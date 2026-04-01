import pandas as pd

# Load the data from the CSV file
file_path = 'data/health_data.csv'
data = pd.read_csv(file_path)

# Print the first 5 rows
print('First 5 rows:')
print(data.head())

# Calculate and print the number of missing values in each column
print('\nNumber of missing values in each column:')
print(data.isnull().sum())
