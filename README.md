# Week 3 — Term Frequency Assignments 

### Commands to run the program
```
python3 eight.py
python3 seven.py
```

This folder has my solutions for EPS 7.1 and EPS 8 from the textbook.
Both programs are written in Python and solve the term frequency problem — basically figuring out which words show up the most in a text file (ignoring common stop words).

### EPS 7.1 — Seven.py
What I did

This one’s the non-recursive version.
I kept it simple:

- I read the text file and a list of stop words.
- Skipped all stop words and one-letter words.
- Counted how often each remaining word appeared.
- Printed out the top 25 most frequent words.


### EPS 8 — Eight.py
What I did

This one’s the recursive version, kind of like how a JSON parser works.
Here, I made a function that:
- Reads the text character by character
- Builds words as it goes
- When it hits a non-letter (like a space or comma), it adds the word to a list (if it’s not a stop word)
- Then keeps going until it hits the end of the file

After that, I just counted and printed the top 25 most common words — same logic, just different parsing.

### Folder setup

Here’s what my folder looks like:

```
Week3/
│
├── Seven.py        # EPS 7.1 - non-recursive term frequency
├── Eight.py        # EPS 8 - recursive term frequency
├── stop_words.txt  # common words to skip
├── input.txt       # text file to analyze
└── README.md       # this file :)
```
### Example output

Both programs print something like this:
```
the - 58
and - 43
of - 41
to - 35
...
```

(Shows the top 25 most frequent words in your input file.)
