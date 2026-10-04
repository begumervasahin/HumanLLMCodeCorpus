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
        doc_set = set(doc_words)
        intersection = query_set.intersection(doc_set)
        positions = [index for index, word in enumerate(doc_words) if word in intersection]
        highlighted_doc = ""
        for i, word in enumerate(doc_words):
            if i in positions:
                highlighted_doc += f'"{word}" '
            else:
                highlighted_doc += word + ' '
        return highlighted_doc.strip()
