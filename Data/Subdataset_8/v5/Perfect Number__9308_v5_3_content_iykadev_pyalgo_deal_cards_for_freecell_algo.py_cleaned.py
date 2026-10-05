	from sys import argv
def linear_congruential_generator(seed=1):
    MAX_INT32 = (1 << 31) - 1
    seed &= MAX_INT32
    while True:
        seed = (seed * 214013 + 2531011) & MAX_INT32
        yield seed >> 16
def shuffle_deck(seed):
    NUM_CARDS = 52
    cards = list(range(NUM_CARDS - 1, -1, -1))
    rng = linear_congruential_generator(seed)
    for i, r in zip(range(NUM_CARDS), rng):
        j = (NUM_CARDS - 1) - r % (NUM_CARDS - i)
        cards[i], cards[j] = cards[j], cards[i]
    return cards
def display_deck(cards):
    card_names = ["A23456789TJQK"[card
    for i in range(0, len(cards), 8):
        print(" ", " ".join(card_names[i : i+8]))
if __name__ == '__main__':
    seed = int(argv[1]) if len(argv) == 2 else 11982
    print("Hand", seed)
    deck = shuffle_deck(seed)
    display_deck(deck)