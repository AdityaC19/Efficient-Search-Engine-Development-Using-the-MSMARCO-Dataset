#!/usr/bin/env python

import sys

# Load the top 10 docIds
top_10 = []
for line in open("test.txt", "r"):
    top_10.append(line.strip().split()[0])  # Take the first index after splitting by whitespace
#print(top_10)
# Function to extract docId, URL, and title from input line
def extract_info(line):
    parts = line.strip().split("\t",2)
    
    if len(parts) == 3:
        doc_id, url, title = parts
	#print(doc_id , url, title)
        return doc_id, url, title
    else:
        return None

# Reduce function
for line in sys.stdin:
    doc_info = extract_info(line)
    if doc_info:
        doc_id, url, title = doc_info
    	if doc_id in top_10:
        	print "{0}\t{1}\t{2}".format(doc_id, url, title)

	
