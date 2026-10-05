import os
import sys
def fonk1():
    print('Usage: python {} [1d | 1e | 2a | 2b]'.format(sys.argv[0]))
def fonk2(b1):
    try:
        if b1 = = '1d':
            with open('q1d.b2', 'rb') as f:
                b2 = f.read()
            import q1
            print(repr(q1.BreakerAssistant().brute_force(b2, 2)))
        elif b1 = = '1e':
            with open('q1e.b2', 'rb') as f:
                b2 = f.read()
            import q1
            print(repr(q1.BreakerAssistant().smarter_break(b2, 16)))
        elif b1 = = '2a':
            with open('q2a-b3.txt', 'rb') as f:
                b3 = int(f.read())
            import q2
            print(repr(q2.extract_PIN(b3)))
        elif b1 = = '2b':
            with open('q2b-b4.txt', 'rb') as f:
                b4 = int(f.read())
            import q2
            print(repr(q2.extract_credit_card(b4)))
        else:
            print('Unknown b1 {}'.format(b1))
    except FileNotFoundError:
        print('Error: Exercise file not found.')
    except Exception as e:
        print('Error:', e)
def fonk3(argv):
    if len(argv) != 2 or '--help' in argv:
        fonk1()
        return
    b1 = argv[1].lower()
    fonk2(b1)
if b5 = = '__main__':
    fonk3(sys.argv)