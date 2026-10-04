import sys
def random_generator(seed=1):
    max_int32 = (1 << 31) - 1
    seed = seed & max_int32
    while True:
        seed = (seed * 214013 + 2531011) & max_int32
        yield seed >> 16
def shuffle_deck(seed):
    num_cards = 52
    cards = list(range(num_cards - 1, -1, -1))
    rnd = random_generator(seed)
    for i, r in zip(range(num_cards), rnd):
        j = (num_cards - 1) - r % (num_cards - i)
        cards[i], cards[j] = cards[j], cards[i]
    return cards
def display_deck(cards):
    ranks = "A23456789TJQK"
    suits = "CDHS"
    card_strs = [ranks[c
    for i in range(0, len(cards), 8):
        print(" ", " ".join(card_strs[i : i + 8]))
def main():
    seed = int(sys.argv[1]) if len(sys.argv) == 2 else 11982
    print(f"Hand {seed}")
    deck = shuffle_deck(seed)
    display_deck(deck)
if __name__ == '__main__':
    main()