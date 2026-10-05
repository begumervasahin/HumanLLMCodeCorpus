import random
class BSTextSearch:
    def __init__(self, text, choice):
        self.text = text
        self.choice = choice
    def start(self):
        print(f"Performing text search: Text='{self.text}', Representation='{self.choice}'")
class BSNumberSearch:
    def __init__(self, number, choice):
        self.number = number
        self.choice = choice
    def start(self):
        print(f"Performing number search: Number={self.number}, Representation='{self.choice}'")
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
class TextLineField:
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
def doTextSearch():
    if get_form_input([_choiceField, _textField], "Text Search"):
        search = BSTextSearch(_textField.result, _choiceField.result)
        search.start()
def doNumberSearch():
    if get_form_input([_choiceField, _numberField], "Number Search"):
        search = BSNumberSearch(int(_numberField.result), _choiceField.result)
        search.start()
def main():
    global _choiceField, _textField, _numberField
    _choiceField = ChoiceField("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
    _textField = TextLineField("Text to search")
    _numberField = TextLineField("Number to search (0x for hex, 0b for binary)")
    doTextSearch()
    doNumberSearch()
if __name__ == "__main__":
    main()