import sys

def reducer():
    seen = set()
    for line in sys.stdin:
        # Ensure uniqueness of docid, url, title, and body snippet combination
        if line not in seen:
            seen.add(line)
            print line.strip()  # Output the line

if __name__ == "__main__":
    reducer()

