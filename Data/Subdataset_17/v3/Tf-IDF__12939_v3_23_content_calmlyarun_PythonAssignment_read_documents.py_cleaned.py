import re
import sys
class Document:
    def __init__(self):
        self.docid = 0
        self.lines = []
    def print_doc(self, out=sys.stdout):
        print(f"\n[DOCID: {self.docid}]", file=out)
        for line in self.lines:
            print(line, file=out)
class ReadDocuments:
    def __init__(self, file_path):
        self.collection_file = file_path
    def __iter__(self):
        startdoc_pattern = re.compile(r'<document docid\s*=\s*"(\d+)"\s*>')
        enddoc_pattern = re.compile(r'</document\s*>')
        reading_doc = False
        with open(self.collection_file, 'r') as file:
            for line in file:
                if not reading_doc:
                    start_match = startdoc_pattern.search(line)
                    if start_match:
                        reading_doc = True
                        doc = Document()
                        doc.docid = int(start_match.group(1))
                else:
                    if enddoc_pattern.search(line):
                        reading_doc = False
                        yield doc
                    else:
                        doc.lines.append(line.strip())
if __name__ == "__main__":
    file_path = 'path_to_your_file.txt'
    reader = ReadDocuments(file_path)
    for document in reader:
        document.print_doc()