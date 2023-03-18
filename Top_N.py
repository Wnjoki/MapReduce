# Define the Map function
def mapper(data):
    # Split the data into key-value pairs
    key, value = data.split(",")
    return (None, (key, int(value)))

# Define the Reduce function
def reducer(key, values):
    # Sort the values in descending order of the value
    sorted_values = sorted(values, key=lambda x: x[1], reverse=True)
    # Return the top N items
    return sorted_values[:N]

# Define the data
data = ["A,50", "B,60", "C,30", "A,20", "B,30", "C,40"]
# Set the value of N
N = 2

# Map the data
mapped_data = map(mapper, data)

# Shuffle and sort the mapped data
sorted_data = sorted(mapped_data)

# Reduce the data
reduced_data = reducer(None, [value for key, value in sorted_data])

# Output the reduced data
print(reduced_data)
