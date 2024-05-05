#!/usr/bin/env python

import sys

# Define BM25Mapper class
class BM25Mapper:
    def __init__(self):
        pass

    def map(self, line):
        # Parse input line and emit intermediate key-value pairs
        word, postings = line.strip().split('\t', 1)
        postings = postings.split(', ')
        for posting in postings:
            doc_id, word_freq = posting.split(':')
            print(f"{doc_id}\t{word}\t{word_freq}")

# Main function for mapper
if __name__ == "__main__":
    mapper = BM25Mapper()
    
    # Process input from standard input (stdin)
    for line in sys.stdin:
        mapper.map(line)
