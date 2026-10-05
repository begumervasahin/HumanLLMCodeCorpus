import random
def linear_congruential_generator(seed=1):
    max_int32 = (1 << 31) - 1
    seed = seed & max_int32
    while True:
        seed = (seed * 214013 + 2531011) & max_int32
        yield seed >> 16
def deal_cards(seed):
    num_cards = 52
    cards = list(range(num_cards - 1, -1, -1))
    rnd = linear_congruential_generator(seed)
    for i, r in zip(range(num_cards), rnd):
        j = (num_cards - 1) - r % (num_cards - i)
        cards[i], cards[j] = cards[j], cards[i]
    return cards
def display_deck(cards):
    card_names = ["A23456789TJQK"[c
    for i in range(0, len(cards), 8):
        print(" ", " ".join(card_names[i: i + 8]))
if __name__ == '__main__':
    seed = int(input("Enter seed: "))
    print("Hand", seed)
    deck = deal_cards(seed)
    display_deck(deck)