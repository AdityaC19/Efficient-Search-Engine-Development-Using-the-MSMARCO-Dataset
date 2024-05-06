import sys
import re

def mapper():
    """
    Read from standard input and process data line by line.
    Each line is assumed to be a record in the form 'doc_id\turl\tcontent'.
    This mapper will also count occurrences of each word in the documents.
    """
    for line in sys.stdin:
        parts = line.strip().split('\t')
        if len(parts) < 3:
            continue  # Skip malformed lines
        doc_id, url, content = parts[0], parts[1], parts[2]
        words = re.findall(r'\w+', content)
        word_count = {}
        for word in words:
            low_word = word.lower()
            if low_word in word_count:
                word_count[low_word] += 1
            else:
                word_count[low_word] = 1
        
        for word, count in word_count.items():
            print "%s\t%s\t%d" % (word, doc_id, count)

if __name__ == "__main__":
    mapper()

