from itertools import groupby


# Define the Map function
def mapper(data):
    key, value = data.split(",")
    return (int(key), value)

# Define the Reduce function
def reducer(key, values):
   
    sorted_values = sorted(values)
    return (key, sorted_values)

# Define the data
data = ["50,A", "60,B", "30,C", "20,A", "30,B", "40,C"]


mapped_data = map(mapper, data)


sorted_data = sorted(mapped_data)

reduced_data = {}
for key, values in groupby(sorted_data, key=lambda x: x[0]):
    reduced_data[key] = reducer(key, [value[1] for value in values])

print(reduced_data)
