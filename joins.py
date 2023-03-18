from functools import reduce
from itertools import groupby
from operator import itemgetter


# Define the Map function for the  datasets
# Split the data into key-value pairs

def mapper1(data):
    
    key, value = data.split(",")
    return (key, ("dataset1", value))

def mapper2(data):
   
    key, value = data.split(",")
    return (key, ("dataset2", value))

def reducer(key, values): #reducer function

    dataset1_values = [value[1] for value in values if value[0] == "dataset1"]
    dataset2_values = [value[1] for value in values if value[0] == "dataset2"]
    #  join operation
    result = [(key, dataset1_value, dataset2_value) for dataset1_value in dataset1_values for dataset2_value in dataset2_values]
    return result

data1 = ["A,50", "B,60", "C,30", "A,20", "B,30", "C,40"]

data2 = ["A,X", "B,Y", "C,Z", "A,Y", "B,X", "C,Z"]

# Map the data for the first dataset
mapped_data1 = map(mapper1, data1)
mapped_data2 = map(mapper2, data2)

# Combine the mapped data
combined_data = list(mapped_data1) + list(mapped_data2)

# Shuffle and sort the combined data by key
sorted_data = sorted(combined_data)

# Reduce the data
reduced_data = {}
for key, values in groupby(sorted_data, key=lambda x: x[0]):
    reduced_data[key] = reducer(key, [value[1] for value in values])

print(reduced_data)
