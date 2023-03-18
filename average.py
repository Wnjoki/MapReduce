from functools import reduce
from itertools import groupby
from operator import itemgetter


# Define the Map function
def mapper(data):
    # Split the data into key-value pairs
    key, value = data.split(",")
    return (key, float(value))

# Define the Reduce function
def reducer(key, values):
    # Calculate the sum and count of the values for each key
    total = sum(values)
    count = len(values)
    # Calculate the average
    average = total / count
    return (key, average)

# Define the data

data = ["A,50", "B,60", "C,30", "A,20", "B,30", "C,40"]

# Map the data
mapped_data = map(mapper, data)

# Shuffle and sort the mapped data by key
sorted_data = sorted(mapped_data)

# Reduce the data
reduced_data = {}
for key, values in groupby(sorted_data, key=lambda x: x[0]):
    reduced_data[key] = reducer(key, [value[1] for value in values])
    
# Output the reduced data
print(reduced_data)
