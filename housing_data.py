import pandas as pd
columns_to_extract = ['LATITUDE', 'LONGITUDE']
selected_columns_df = pd.read_csv('Affordable_Housing.csv', usecols=columns_to_extract)

# Write the DataFrame to a CSV file
output_csv_file = 'housing_coordinates.csv'
selected_columns_df.to_csv(output_csv_file, index=False)

print(f"DataFrame with selected columns written to '{output_csv_file}' successfully.")

