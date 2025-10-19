import sys

# Read stop words and return as a set
def stop():
    return set(open("stop_words.txt").read().split(","))

# Recursive scanner to collect words
def scan(txt, i, words, st, word):
    if i >= len(txt):
        if word and word not in st:
            words.append(word)
        return words
    c = txt[i]
    if c.isalnum():  # keep building word
        return scan(txt, i + 1, words, st, word + c.lower())
    else:  # non-alphanumeric → end of word
        if word and word not in st:
            words.append(word)
        return scan(txt, i + 1, words, st, "")

# Read input file and collect words
text = list(open("input.txt", "r").read())
s = stop()
lst = scan(text, 0, [], s, "")

# Count word frequencies
d = {}
for w in lst:
    d[w] = d.get(w, 0) + 1

# Sort and print top 25
z = sorted(d.items(), key=lambda x: -x[1])
for a, b in z[:25]:
    print(a, "-", b)
