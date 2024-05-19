import pandas as pd

# Read the CSV data file from the zip archive
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

# Group by country and calculate the number of reviews and average points
summary = df.groupby('country').agg(
    count=('country', 'size'),
    points=('points', 'mean')
).reset_index()

# Round the points column to 1 decimal place
summary['points'] = summary['points'].round(1)

# Save the summary to a new CSV file in the data folder
summary.to_csv('data/reviews-per-country.csv', index=False)