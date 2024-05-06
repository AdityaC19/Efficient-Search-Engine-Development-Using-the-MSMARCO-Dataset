# MSMARCO Search Engine Project

## Project Overview
This project aims to develop an efficient search engine utilizing the MSMARCO Dataset. The primary focus is on constructing an inversion tree to enable quick and accurate information retrieval from a vast repository of digital data. Our approach leverages advanced indexing techniques and optimized memory management to handle large-scale datasets effectively.

## Key Features
- **Inversion Tree Indexing:** Fast and efficient indexing of documents using an inversion tree structure.
- **BM25 Ranking Algorithm:** Implementation of the BM25 algorithm to improve the relevance of search results.
- **Memory Efficiency:** Techniques for managing memory when processing large datasets, ensuring stability and performance.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Access to MSMARCO dataset files

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/msmarco-search-engine.git
cd msmarco-search-engine
```

## Architecture

This section describes the architecture of the search engine, detailing the mapper and reducer scripts used to process and index the MSMARCO dataset.

### Mapper
The mapper script (`mapper_inversionTree.py`) reads and processes input data to extract words and emit them alongside their document ID and occurrence count.

### Reducer
The reducer script (`reducer_inversionTree.py`) aggregates the output from the mapper, compiling and organizing each word into an inversion tree which forms the basis for the search index.
