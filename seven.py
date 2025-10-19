# Read stop words and input text
t = open("stop_words.txt").read().split(",")
w = open("input.txt").read().lower().split()

f = {}  # word frequency map

# Count words not in stop list
for x in w:
    if len(x) > 1 and x not in t:
        f[x] = f.get(x, 0) + 1

# Sort by frequency (descending)
s = sorted(f.items(), key=lambda x: -x[1])

# Print top 25
for a, b in s[:25]:
    print(a, "-", b)