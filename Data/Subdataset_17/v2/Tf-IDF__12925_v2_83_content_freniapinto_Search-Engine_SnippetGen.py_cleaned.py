class FileAccess:
    def get_stop_words(self):
        return ['the', 'is', 'in', 'at', 'of', 'a', 'and']
class SnippetGenerator:
    def __init__(self, max_length=150):
        self.max_length = max_length
    def generate_snippet(self, doc, query):
        fa = FileAccess()
        stop_words = fa.get_stop_words()
        query_words = [word for word in query.split() if word not in stop_words]
        doc_words = doc.split()
        positions = [i for i, word in enumerate(doc_words) if word in query_words]
        highlighted_doc = ' '.join(
            ['"' + word + '"' if i in positions else word for i, word in enumerate(doc_words)]
        )
        return highlighted_doc
if __name__ == "__main__":
    doc = "This is an example document that contains several words and we will highlight some of them."
    query = "example document highlight"
    snippet_generator = SnippetGenerator()
    snippet = snippet_generator.generate_snippet(doc, query)
    print(snippet)