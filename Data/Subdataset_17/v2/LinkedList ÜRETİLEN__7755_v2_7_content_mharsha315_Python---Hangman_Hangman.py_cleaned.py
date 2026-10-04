import random
import time
class Node:
    def __init__(self, data="-", datacheck="-"):
        """
        Initialize a new node with the given data.
        Args:
            data: The character to store in the node.
            datacheck: The character to display in the current state. Default is "-".
        Initialize a new game with an empty linked list.
        Insert the given word into the linked list.
        Args:
            word: The word to insert into the linked list.
        Display the current state of the word.
        """
        current = self.head.next
        print("\nCurrent state of the word:")
        while current:
            print(current.datacheck, end=" ")
            current = current.next
        print()
    def play(self, guess, hangman):
        found = False
        current = self.head.next
        while current:
            if current.data == guess:
                current.datacheck = guess
                found = True
            current = current.next
        if not found:
            hangman.pop(0)
        self.display()
        print("Remaining chances: ", ''.join(hangman))
    def view_answer(self):
        current = self.head.next
        print("ANSWER IS...")
        time.sleep(2.0)
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
def play_game():
    game = Game()
    words = [
        "python", "jumble", "easy", "difficult", "computer", "hangman", "failure", "brilliant", "worthy",
        "xylophone", "awkward", "gypsy", "jinx", "burglar", "bankrupt", "crisis", "hyphen", "memento", "mystery",
        "pajama", "pixel", "rogue", "rhythmic", "twelfth", "jealous", "zombie", "yacht", "yak", "zippy", "unknown",
        "battleground", "player", "psycho", "beast", "buzzard", "boycott", "coffin", "witchcraft", "rickshaw",
        "mnemonic", "pneumonia", "peekaboo", "diarrhea", "jaundice", "gossip", "despacito"
    ]
    selected_word = random.choice(words)
    game.insert(selected_word)
    game.display()
    hangman = ["H", "A", "N", "G", "M", "A", "N"]
    while True:
        user_input = input("Enter your guess or command (view/exit): ").strip().lower()
        if user_input == "exit":
            print("Exiting...")
            break
        elif user_input == "view":
            game.view_answer()
            break
        elif len(hangman) == 0:
            print("You've run out of chances!")
            game.view_answer()
            break
        else:
            game.play(user_input, hangman)
def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break
if __name__ == "__main__":
    main()