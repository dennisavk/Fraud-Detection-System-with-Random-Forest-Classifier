import pandas as pd

# Step 1: Load the CSV file
df = pd.read_csv('data/application_data.csv')  # Update the file path to your actual CSV file

# Step 2: Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Optional: Fill missing values or drop rows with missing data
df = df.fillna(0)  # Replace missing values with 0 (or choose other strategies)

# Step 3: Convert string columns to categorical (numeric) values
for column in df.columns:
    if df[column].dtype == 'object':  # If the column is of type string
        df[column] = pd.Categorical(df[column]).codes  # Convert to categorical numeric codes

# Step 4: View the first few rows of the DataFrame to verify
print("Processed data:")
print(df.head())

# Optional: Save the cleaned data to a new CSV file
df.to_csv('processed_fraud_detection.csv', index=False)

# Optional: Display DataFrame info (types, non-null counts)
print(df.info())

