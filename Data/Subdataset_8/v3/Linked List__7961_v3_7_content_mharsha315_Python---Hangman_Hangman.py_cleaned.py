import random
import time
class Node:
    def __init__(self, data="-", datacheck="-"):
        self.data = data
        self.datacheck = datacheck
        self.next = None
class HangmanGame:
    def __init__(self):
        self.head = Node()
    def insert_word(self, word):
        current = self.head
        for letter in word:
            new_node = Node(letter)
            current.next = new_node
            current = current.next
    def display_word(self):
        current = self.head.next
        print()
        while current is not None:
            print(current.datacheck, end="")
            current = current.next
        print()
    def play_game(self, letter, hangman):
        found = False
        current = self.head.next
        while current is not None:
            if current.data == letter:
                current.datacheck = letter
                found = True
            current = current.next
        if not found:
            hangman.pop(0)
        current = self.head.next
        while current is not None:
            print(current.datacheck, end="")
            current = current.next
        print(hangman)
    def view_answer(self):
        current = self.head.next
        print("ANSWER IS...")
        time.sleep(2.0)
        while current is not None:
            print(current.data, end="")
            current = current.next
def start_game():
    hangman_game = HangmanGame()
    print("Type 'view' to view the answer")
    print("Type 'exit' to EXIT")
    words = [
        "python", "jumble", "easy", "difficult", "computer", "hangman", "failure", "brilliant", "worthy",
        "xylophone", "awkward", "gypsy", "jinx", "burglar", "bankrupt", "crisis", "hyphen", "memento", "mystery",
        "pajama", "pixel", "rogue", "rhythmic", "twelfth", "jealous", "zombie", "yacht", "yak", "zippy", "unknown",
        "battleground", "player", "psycho", "beast", "buzzard", "boycott", "coffin", "witchcraft", "rickshaw",
        "mnemonic", "pneumonia", "peekaboo", "diarrhoea", "jaundice", "gossip", "despacito"
    ]
    word = [random.choice(words)]
    hangman_game.insert_word(word)
    hangman_game.display_word()
    hangman = ["H", "A", "N", "G", "M", "A", "N"]
    while len(hangman) != 0:
        user_input = input()
        if user_input != "exit" and user_input != "view":
            hangman_game.play_game(user_input, hangman)
        elif user_input == "view":
            hangman_game.view_answer()
            break
        elif user_input == "exit":
            print("Exiting...")
            break
def play_again():
    return input("Do you want to play again? (yes/no): ").lower()
def main():
    start_game()
    while play_again() == "yes":
        start_game()
if __name__ == "__main__":
    main()