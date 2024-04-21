import matplotlib.pyplot as plt
import numpy as np

# Read data from the text file
data = {}
with open('states_corr.txt', 'r') as file:
    for line in file:
        state, value = line.strip().split(' ')
        data[state] = float(value)

# Extract state names and values
states = list(data.keys())
values = list(data.values())

# Define state codes and corresponding values
state_codes = ['WI', 'WV', 'VT', 'TX', 'SD', 'RI', 'OR', 'NY', 'NH', 'NE', 'KS', 'MS', 'IL', 'DE', 'CT', 'AR', 'IN', 'MO', 'FL', 'NV', 'ME', 'MI', 'GA', 'HI', 'AK', 'TN', 'VA', 'NJ', 'KY', 'ND', 'MN', 'OK', 'MT', 'WA', 'UT', 'CO', 'OH', 'AL', 'IA', 'NM', 'SC', 'PA', 'AZ', 'MD', 'MA'] 
state_codes.sort() 
state_values = [data[state] if state in data else 0 for state in state_codes]

# Plot the heat map
plt.figure(figsize=(12, 8))
plt.scatter(range(len(state_codes)), [1]*len(state_codes), c=state_values, cmap='hot', s=1000, marker='s')
plt.xticks(range(len(state_codes)), state_codes, rotation=90)
plt.colorbar(label='Value') 
plt.title('Heat Map of State Values')
plt.tight_layout()
plt.show()
