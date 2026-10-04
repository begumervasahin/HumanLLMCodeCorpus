from FileAccess import FileAccess
class SnippetGenerator:
    def __init__(self):
        self.max = 150
    def generate_snippet(self, doc, query):
        fa = FileAccess()
        stop_words = fa.get_stop_words()
        query_words = query.split()
        filtered_query = [word for word in query_words if word not in stop_words]
        query_set = set(filtered_query)
        doc_words = doc.split()
        intersection = query_set.intersection(doc_words)
        positions = [index for index, word in enumerate(doc_words) if word in intersection]
        highlighted_doc = " ".join(
            f'"{word}"' if i in positions else word
            for i, word in enumerate(doc_words)
        )
        return highlighted_doc.strip()
