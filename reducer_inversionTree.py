import sys

def reducer():
    current_word = None
    doc_dict = {}

    for line in sys.stdin:
        parts = line.strip().split('\t')
        if len(parts) < 3:
            continue  # Skip malformed lines
        word, doc_id, count = parts[0], parts[1], int(parts[2])
        if word == current_word:
            if doc_id in doc_dict:
                doc_dict[doc_id] += count
            else:
                doc_dict[doc_id] = count
        else:
            if current_word is not None:
                # Emit the current word and all associated document IDs with counts
                print "%s\t%s" % (current_word, ', '.join(['%s:%d' % (doc, c) for doc, c in doc_dict.items()]))
            current_word = word
            doc_dict = {doc_id: count}

    # Output the last word if necessary
    if current_word is not None:
        print "%s\t%s" % (current_word, ', '.join(['%s:%d' % (doc, c) for doc, c in doc_dict.items()]))

if __name__ == "__main__":
    reducer()

