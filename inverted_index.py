
from itertools import groupby

# Define the Map function
def mapper(data):
    
    document_id, text = data.split("|")
    words = text.split(",")
    # Emit each word with its corresponding document ID
    for word in words:
        yield (word, document_id)

# Define the Reduce function
def reducer(key, values):
    # Aggregate the document IDs for each word
    document_ids = set(values)
    return (key, list(document_ids))

# Define the data
data = [
   "austen.txt| Emma Woodhouse, handsome, clever, and rich, with a...", 
   "edgeworth.txt | Near the ruins of the castle of Rossmore, in Ireland...",
   "chesterton.txt|The flying ship of Professor Lucifer sang through the skies like...",
   "shakespeare.txt| Actus Primus, Scoena Prima, Enter Flaulus, Murellus, and...."
]

mapped_data = map(mapper, data)


sorted_data = sorted(mapped_data)

# Reduce the data
reduced_data = {}
for key, values in groupby(sorted_data, key=lambda x: x[0]):
    reduced_data[key] = reducer(key, [value[1] for value in values])
    
# Output the reduced data
print(reduced_data)
