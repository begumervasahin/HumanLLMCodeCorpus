import shelve
class QuestionNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class QuestionTree:
    def __init__(self):
        self.root = QuestionNode("hippo")
    def play_game(self):
        print("Welcome to 20 Questions.")
        self.root = self.play_game_helper(self.root)
    def play_game_helper(self, node):
        if node.left is None and node.right is None:
            print("You're thinking of:", node.data)
            response = input("Is it correct (y/n)? ").strip().lower()
            if response == "y":
                print("I win!!")
                return node
            else:
                return self.add_answer(node)
        else:
            print(node.data)
            response = input("y/n? ").strip().lower()
            if response == "y":
                node.right = self.play_game_helper(node.right)
            elif response == "n":
                node.left = self.play_game_helper(node.left)
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                return self.play_game_helper(node)
            return node
    def add_answer(self, old_node):
        your_thing = input("Enter the thing you were thinking of: ").strip()
        question = input("Enter your disambiguating question: ").strip()
        yes_or_no = input("Is your thing the answer to the question (y/n)? ").strip().lower()
        your_thing_node = QuestionNode(your_thing)
        new_question_node = QuestionNode(question)
        if yes_or_no == "y":
            new_question_node.right = your_thing_node
            new_question_node.left = old_node
        elif yes_or_no == "n":
            new_question_node.right = old_node
            new_question_node.left = your_thing_node
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            return self.add_answer(old_node)
        return new_question_node
def main():
    savefile = shelve.open("twenty_questions.save")
    if "tree" in savefile:
        twenty_questions = savefile["tree"]
    else:
        twenty_questions = QuestionTree()
    twenty_questions.play_game()
    keep_playing = True
    while keep_playing:
        savefile["tree"] = twenty_questions
        response = input("Do you want to play again (y/n)? ").strip().lower()
        if response == "y":
            twenty_questions.play_game()
        elif response == "n":
            print("Thanks for playing! Goodbye.")
            keep_playing = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    savefile.close()
if __name__ == "__main__":
    main()