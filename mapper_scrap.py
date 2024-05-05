#!/usr/bin/env python

import sys

# Function to extract docId, URL, and title from input line
def extract_info(line):
    try:
        parts = line.strip().split("\t", 2)  # Limit the split to 3
        if len(parts) == 3:
            doc_id, url, title = parts
            return doc_id, url, title
        else:
            return None
    except Exception as e:
        # If an error occurs, return None
        return None

# Map function
for line in sys.stdin:
    doc_info = extract_info(line)
    if doc_info:
        doc_id, url, title = doc_info
        print "{0}\t{1}\t{2}".format(doc_id, url, title)

