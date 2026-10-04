import random
import time
class Node:
    def __init__(self, data="-", datacheck="-"):
        self.data = data
        self.datacheck = datacheck
        self.next = None
class Game:
    def __init__(self):
        self.head = Node()
    def insert(self, word):
        pos = self.head
        for char in word:
            new_node = Node(char)
            pos.next = new_node
            pos = new_node
    def display(self):
        pos = self.head.next
        print("\n", end="")
        while pos:
            print(pos.datacheck, end="")
            pos = pos.next
        print()
    def play(self, guess, hangman_state):
        flag = False
        pos = self.head.next
        while pos:
            if pos.data == guess:
                pos.datacheck = guess
                flag = True
            pos = pos.next
        if not flag:
            hangman_state.pop(0)
        self.display()
        print(hangman_state)
    def view_answer(self):
        pos = self.head.next
        print("ANSWER IS...")
        time.sleep(2.0)
        while pos:
            print(pos.data, end="")
            pos = pos.next
        print()
def option():
    game = Game()
    print("Type 'view' to view answer")
    print("Type 'exit' to EXIT")
    word_list = [
        "python", "jumble", "easy", "difficult", "computer", "hangman", "failure", "brilliant", "worthy", "xylophone",
        "awkward", "gypsy", "jinx", "burglar", "bankrupt", "crisis", "hyphen", "memento", "mystery", "pajama", "pixel",
        "rogue", "rhythmic", "twelfth", "jealous", "zombie", "yacht", "yak", "zippy", "unknown", "battleground",
        "player", "psycho", "beast", "buzzard", "boycott", "coffin", "witchcraft", "rickshaw", "mnemonic", "pneumonia",
        "peekaboo", "diarrhea", "jaundice", "gossip", "despacito"
    ]
    chosen_word = random.choice(word_list)
    game.insert(chosen_word)
    game.display()
    hangman_state = ["H", "A", "N", "G", "M", "A", "N"]
    while hangman_state:
        user_input = input().strip().lower()
        if user_input == "exit":
            print("Exiting...")
            break
        elif user_input == "view":
            game.view_answer()
            break
        else:
            game.play(user_input, hangman_state)
def main():
    print("Welcome to Hangman!")
    play_again = "yes"
    while play_again == "yes":
        option()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    print("Thank you for playing!")
if __name__ == "__main__":
    main()