import copy
def fonk1(b11, b20, b21):
    b1 = {v: k for k, v in b11.items()}
    for she, he in b11.items():
        b2 = b21[she]
        b3 = b2[:b2.index(he)]
        b4 = b20[he]
        b5 = b4[:b4.index(she)]
        for b14 in b3:
            b6 = b1[b14]
            b7 = b20[b14]
            if b7.index(b6) > b7.index(she):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (she, b14, he, b6))
                return False
        for b16 in b5:
            b8 = b11[b16]
            b9 = b21[b16]
            if b9.index(b8) > b9.index(he):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (he, b16, she, b8))
                return False
    return True
def fonk2(b20, b21):
    b10 = list(b20.keys())
    b11 = {}
    b12 = copy.deepcopy(b20)
    b13 = copy.deepcopy(b21)
    while b10:
        b14 = b10.pop(0)
        b15 = b12[b14]
        b16 = b15.pop(0)
        b17 = b11.get(b16)
        if not b17:
            b11[b16] = b14
            print("  %s and %s" % (b14, b16))
        else:
            b18 = b13[b16]
            if b18.index(b17) > b18.index(b14):
                b11[b16] = b14
                print("  %s dumped %s for %s" % (b16, b17, b14))
                if b12[b17]:
                    b10.append(b17)
            else:
                if b15:
                    b10.append(b14)
    return b11
if b19 = = '__main__':
    b20 = {
        'abe': ['abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
        'bob': ['cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
        'col': ['hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
        'dan': ['ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
        'ed': ['jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
        'fred': ['bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
        'gav': ['gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
        'hal': ['abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
        'ian': ['hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
        'jon': ['abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope']
    }
    b21 = {
        'abi': ['bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
        'bea': ['bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
        'cath': ['fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
        'dee': ['fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed'],
        'eve': ['jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob'],
        'fay': ['bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal'],
        'gay': ['jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian'],
        'hope': ['gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred'],
        'ivy': ['ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan'],
        'jan': ['ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan']
    }
    print('\nEngagements:')
    b11 = fonk2(b20, b21)
    print('\nCouples:')
    print('  ' + ',\n  '.join('%s is b11 to %s' % couple
                              for couple in sorted(b11.items())))
    print()
    print('Engagement stability check PASSED' if fonk1(b11, b20, b21)
          else 'Engagement stability check FAILED')