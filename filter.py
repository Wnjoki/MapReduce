# Define the Map function
def mapper(data):
    # Split the data into key-value pairs
    key, value = data.split(",")
    # Check if the value meets the filtering criteria
    if float(value) > 30:
        return (key, value)
    else:
        return None

# Define the Reduce function
def reducer(key, values):
    
    return None

# Define the data
data = ["A,50", "B,60", "C,30", "A,20", "B,30", "C,40"]

# Map the data
mapped_data = map(mapper, data)

# Filter the data by removing any None values
filtered_data = list(filter(None, mapped_data))

# Output the filtered data
print(filtered_data)
