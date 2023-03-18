from itertools import groupby

# Define the Map function
def mapper(data):
    
    key, value = data.split(",")
    return (int(value) // 5, 1)

# Define the Reduce function
def reducer(key, values):

    count = sum(values)
    return (key, count)

# Define the data
data =  ["A,50", "B,60", "C,30", "A,20", "B,30", "C,40"]

mapped_data = map(mapper, data)


sorted_data = sorted(mapped_data)

# Reduce the data
reduced_data = {}
for key, values in groupby(sorted_data, key=lambda x: x[0]):
    reduced_data[key] = reducer(key, [value[1] for value in values])
    
print(reduced_data)
