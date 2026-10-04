class FileAccess:
    def get_stop_words(self):
        return ['the', 'is', 'in', 'at', 'of', 'a', 'and']
class SnippetGenerator:
    def __init__(self, max_length=150):
        self.max_length = max_length
    def generate_snippet(self, doc, query):
        fa = FileAccess()
        stop_words = fa.get_stop_words()
        query_words = self._remove_stop_words(query, stop_words)
        positions = self._find_query_positions(doc, query_words)
        highlighted_doc = self._highlight_words(doc, positions)
        return highlighted_doc
    def _remove_stop_words(self, query, stop_words):
        return [word for word in query.split() if word not in stop_words]
    def _find_query_positions(self, doc, query_words):
        doc_words = doc.split()
        return [i for i, word in enumerate(doc_words) if word in query_words]
    def _highlight_words(self, doc, positions):
        doc_words = doc.split()
        return ' '.join(
            ['"' + word + '"' if i in positions else word for i, word in enumerate(doc_words)]
        )
if __name__ == "__main__":
    doc = "This is an example document that contains several words and we will highlight some of them."
    query = "example document highlight"
    snippet_generator = SnippetGenerator()
    snippet = snippet_generator.generate_snippet(doc, query)
    print(snippet)