# Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

# Count word frequency
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1  # get method(key, default value if key not found)

# Find the most common word
bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
