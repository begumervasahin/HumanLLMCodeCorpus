class Search:
    def __init__(self, query, representation):
        self.query = query
        self.representation = representation
    def start(self):
        print(f"Performing {self.__class__.__name__}: Query='{self.query}', Representation='{self.representation}'")
class ChoiceField:
    def __init__(self, label, options):
        self.label = label
        self.options = options
        self.result = None
    def show(self):
        print(f"{self.label}: {self.options}")
        choice = input("Enter your choice: ")
        if choice in self.options:
            self.result = choice
        else:
            print("Invalid choice.")
class TextField:
    def __init__(self, label):
        self.label = label
        self.result = None
    def show(self):
        self.result = input(f"Enter {self.label}: ")
def get_form_input(fields, title):
    print(title)
    for field in fields:
        field.show()
        if field.result is None:
            return False
    return True
def perform_search(search_type, query_field, representation_field, title):
    if get_form_input([representation_field, query_field], title):
        search = search_type(query_field.result, representation_field.result)
        search.start()
def main():
    representation_field = ChoiceField("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
    text_field = TextField("Text to search")
    number_field = TextField("Number to search (0x for hex, 0b for binary)")
    perform_search(Search, text_field, representation_field, "Text Search")
    perform_search(Search, number_field, representation_field, "Number Search")
if __name__ == "__main__":
    main()