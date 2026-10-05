class TextSearch:
    def __init__(self, text, representation):
        self.text = text
        self.representation = representation
    def start(self):
        print(f"Performing text search: Text='{self.text}', Representation='{self.representation}'")
class NumberSearch:
    def __init__(self, number, representation):
        self.number = number
        self.representation = representation
    def start(self):
        print(f"Performing number search: Number={self.number}, Representation='{self.representation}'")
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
class TextInputField:
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
def perform_text_search():
    if get_form_input([choice_field, text_field], "Text Search"):
        search = TextSearch(text_field.result, choice_field.result)
        search.start()
def perform_number_search():
    if get_form_input([choice_field, number_field], "Number Search"):
        search = NumberSearch(int(number_field.result), choice_field.result)
        search.start()
def main():
    global choice_field, text_field, number_field
    choice_field = ChoiceField("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
    text_field = TextInputField("Text to search")
    number_field = TextInputField("Number to search (0x for hex, 0b for binary)")
    perform_text_search()
    perform_number_search()
if __name__ == "__main__":
    main()