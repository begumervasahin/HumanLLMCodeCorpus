import os
import sys
def fonk1(argv):
    if len(argv) != 2 or '--help' in argv:
        print('Usage: python %s [1d | 1e | 2a | 2b]' % (argv[0] if argv else __file__))
        return
    b1 = argv[1].lower()
    b2 = os.path.dirname(__file__)
    if b1 = = '1d':
        with open('q1d.b3', 'rb') as f:
            b3 = f.read()
        import q1
        print(repr(q1.BreakerAssistant().brute_force(b3, 2)))
    elif b1 = = '1e':
        with open('q1e.b3', 'rb') as f:
            b3 = f.read()
        import q1
        print(repr(q1.BreakerAssistant().smarter_break(b3, 16)))
    elif b1 = = '2a':
        with open('q2a-b4.txt', 'rb') as f:
            b4 = int(f.read())
        import q2
        print(repr(q2.extract_PIN(b4)))
    elif b1 = = '2b':
        with open('q2b-b5.txt', 'rb') as f:
            b5 = int(f.read())
        import q2
        print(repr(q2.extract_credit_card(b5)))
    else:
        print('Unknown exercise %s' % b1)
if b6 = = '__main__':
    fonk1(sys.argv)