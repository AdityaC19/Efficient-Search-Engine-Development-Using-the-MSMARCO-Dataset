#!/usr/bin/env python

import sys
import math
import os

# Define BM25Reducer class
class BM25Reducer:
    def __init__(self):
        self.inversion_tree = {}

    def reduce(self, lines):
        # Initialize a dictionary to store word frequencies for each document
        self.inversion_tree = {}

        # Aggregate word frequencies for each document ID
        for line in lines:
            doc_id, word, word_freq = line.strip().split('\t', 2)
            if doc_id not in self.inversion_tree:
                self.inversion_tree[doc_id] = {}
            self.inversion_tree[doc_id][word] = self.inversion_tree[doc_id].get(word, 0) + int(word_freq)

    def calculate_idf(self, term, query_terms, document_count):
        # Calculate IDF
        document_with_term_count = len(self.inversion_tree[term])
        query_term_freq = query_terms[term]
        return math.log((document_count - document_with_term_count + 0.5) / (document_with_term_count + 0.5) + 1) * query_term_freq

    def calculate_bm25_score(self, query, document, doc_id, document_count, avg_document_length):
        # Calculate BM25 score
        score = 0.0
        document_length = sum(document.values())
        query_terms = {}
        for term in query:
            query_terms[term] = query_terms.get(term, 0) + 1

        for term in query_terms:
            if term not in self.inversion_tree:
                continue
            idf = self.calculate_idf(term, query_terms, document_count)
            word_frequencies = self.inversion_tree[term]
            term_frequency = word_frequencies.get(doc_id, 0)
            k1 = 1.2
            b = 0.75
            numerator = term_frequency * (k1 + 1)
            denominator = term_frequency + (k1 * (1 - b + b * (document_length / avg_document_length)))
            score += idf * (numerator / denominator)

        return doc_id, score

# Main function for reducer
if __name__ == "__main__":
    reducer = BM25Reducer()
    
    # Read input from standard input (stdin)
    lines = sys.stdin.readlines()
    
    # Process input lines
    reducer.reduce(lines)

    # Calculate BM25 scores and print results
    # Read query input from user
    try:
        query = os.environ.get("QUERY", "").split()
    except EOFError:
        print "Error: No query input provided. Exiting."
        sys.exit(1)

    document_count = len(reducer.inversion_tree)
    avg_document_length = sum(sum(doc.values()) for doc in reducer.inversion_tree.values()) / document_count

    for doc_id in reducer.inversion_tree:
        doc_score = reducer.calculate_bm25_score(query, reducer.inversion_tree[doc_id], doc_id, document_count, avg_document_length)
        print(f"{doc_score[0]}\t{doc_score[1]}")
