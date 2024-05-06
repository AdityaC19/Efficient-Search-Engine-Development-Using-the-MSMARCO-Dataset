import sys

def mapper():
    for line in sys.stdin:
        # Split the line into components based on tab separation
        parts = line.strip().split('\t')
        
        # Check if we have enough parts to include a title and body
        if len(parts) >= 4:
            docid = parts[0]
            url = parts[1]
            title = parts[2]
            body = parts[3][:100]  # Get first 100 characters of the body
            
            # Print out the results as tab-separated values
            print '%s\t%s\t%s\t%s' % (docid, url, title, body)

if __name__ == "__main__":
    mapper()

