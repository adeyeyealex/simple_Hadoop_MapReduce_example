#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # changing to lowercase
    line = line.lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    stopwords = set(['the', 'and', '.', ',', '-', '_', ])

    for word in words:
        if word not in stopwords:
          print '%s\t%s' % (word, "1")
