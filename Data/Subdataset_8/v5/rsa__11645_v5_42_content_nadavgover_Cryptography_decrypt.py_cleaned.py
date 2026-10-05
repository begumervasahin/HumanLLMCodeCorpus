import os
import sys
def print_usage():
    print('Usage: python {} [1d | 1e | 2a | 2b]'.format(sys.argv[0]))
def process_exercise(exercise):
    try:
        if exercise == '1d':
            with open('q1d.cipher', 'rb') as f:
                cipher = f.read()
            import q1
            print(repr(q1.BreakerAssistant().brute_force(cipher, 2)))
        elif exercise == '1e':
            with open('q1e.cipher', 'rb') as f:
                cipher = f.read()
            import q1
            print(repr(q1.BreakerAssistant().smarter_break(cipher, 16)))
        elif exercise == '2a':
            with open('q2a-pin.txt', 'rb') as f:
                pin = int(f.read())
            import q2
            print(repr(q2.extract_PIN(pin)))
        elif exercise == '2b':
            with open('q2b-card.txt', 'rb') as f:
                card = int(f.read())
            import q2
            print(repr(q2.extract_credit_card(card)))
        else:
            print('Unknown exercise {}'.format(exercise))
    except FileNotFoundError:
        print('Error: Exercise file not found.')
    except Exception as e:
        print('Error:', e)
def main(argv):
    if len(argv) != 2 or '--help' in argv:
        print_usage()
        return
    exercise = argv[1].lower()
    process_exercise(exercise)
if __name__ == '__main__':
    main(sys.argv)