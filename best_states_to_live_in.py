
top_15_affordable_states = ['MS', 'OK', 'KS', 'MO', 'AL', 'IA', 'NE', 'WV', 'AR', 'TN', 'IL', 'GA', 'IN', 'LA', 'MI'] 

# Read data from the text file
data = {}
with open('states_corr.txt', 'r') as file:
    for line in file:
        state, value = line.strip().split(' ')
        data[state] = float(value)

# Sort the data dictionary by values
sorted_data = sorted(data.items(), key=lambda x: x[1])

# Get the top 15 states with the least values
top_15_states = sorted_data[:15] 

top_15_states_array = []

# Print the top 15 states
for state, value in top_15_states:
    top_15_states_array.append(state) 


set1 = set(top_15_affordable_states) 
set2 = set(top_15_states_array) 

common_values = set1.intersection(set2) 
common_values_list = list(common_values) 

print(common_values_list)

