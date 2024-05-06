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



## Ranking documents with BM25 algorithm

Hadoop command to run BM25 MapReduce program\
Edit the command to input your query at -cmdenv QUERY="Your query here"\
Check below:
```bash
hadoop jar $HADOOP_HOME/hadoop-streaming-3.2.3.jar     -input gs://nyu-dataproc-hdfs-ingest/output_project.txt    -output BM25_ranking_output     -mapper "python BM25_mapper.py"     -reducer "python BM25_reducer3.py"     -file BM25_mapper.py     -file BM25_reducer3.py  -cmdenv QUERY="Your query here"
```

Then concat the output using
```bash
hdfs dfs -cat BM25_ranking_output/part* | sort > BM25_output.txt
```


## Mapping 
doc_id to corresponding url and title we will use hadoop map reduce
```bash
hadoop jar $HADOOP_HOME/hadoop-streaming-3.2.3.jar     -input gs://nyu-dataproc-hdfs-ingest/scrap.txt    -output BM25Top10     -mapper "python mapper_scrap.py"     -reducer "python reducer_scrap.py"     -file mapper_scrap.py     -file reducer_scrap.py  -file test.txt
```
And after getting the output we will concat them using 

```bash
hdfs dfs -cat BM25Top10/part*
```
