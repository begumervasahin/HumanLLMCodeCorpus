import copy
b1 = {
 'abe':  ['abi', 'eve', 'cath', 'ivy', 'jan', 'dee', 'fay', 'bea', 'hope', 'gay'],
 'bob':  ['cath', 'hope', 'abi', 'dee', 'eve', 'fay', 'bea', 'jan', 'ivy', 'gay'],
 'col':  ['hope', 'eve', 'abi', 'dee', 'bea', 'fay', 'ivy', 'gay', 'cath', 'jan'],
 'dan':  ['ivy', 'fay', 'dee', 'gay', 'hope', 'eve', 'jan', 'bea', 'cath', 'abi'],
 'ed':   ['jan', 'dee', 'bea', 'cath', 'fay', 'eve', 'abi', 'ivy', 'hope', 'gay'],
 'fred': ['bea', 'abi', 'dee', 'gay', 'eve', 'ivy', 'cath', 'jan', 'hope', 'fay'],
 'gav':  ['gay', 'eve', 'ivy', 'bea', 'cath', 'abi', 'dee', 'hope', 'jan', 'fay'],
 'hal':  ['abi', 'eve', 'hope', 'fay', 'ivy', 'cath', 'jan', 'bea', 'gay', 'dee'],
 'ian':  ['hope', 'cath', 'dee', 'gay', 'bea', 'abi', 'fay', 'ivy', 'jan', 'eve'],
 'jon':  ['abi', 'fay', 'jan', 'gay', 'eve', 'bea', 'dee', 'cath', 'ivy', 'hope']}
b2 = {
 'abi':  ['bob', 'fred', 'jon', 'gav', 'ian', 'abe', 'dan', 'ed', 'col', 'hal'],
 'bea':  ['bob', 'abe', 'col', 'fred', 'gav', 'dan', 'ian', 'ed', 'jon', 'hal'],
 'cath': ['fred', 'bob', 'ed', 'gav', 'hal', 'col', 'ian', 'abe', 'dan', 'jon'],
 'dee':  ['fred', 'jon', 'col', 'abe', 'ian', 'hal', 'gav', 'dan', 'bob', 'ed'],
 'eve':  ['jon', 'hal', 'fred', 'dan', 'abe', 'gav', 'col', 'ed', 'ian', 'bob'],
 'fay':  ['bob', 'abe', 'ed', 'ian', 'jon', 'dan', 'fred', 'gav', 'col', 'hal'],
 'gay':  ['jon', 'gav', 'hal', 'fred', 'bob', 'abe', 'col', 'ed', 'dan', 'ian'],
 'hope': ['gav', 'jon', 'bob', 'abe', 'ian', 'dan', 'hal', 'ed', 'col', 'fred'],
 'ivy':  ['ian', 'col', 'hal', 'gav', 'fred', 'bob', 'abe', 'ed', 'jon', 'dan'],
 'jan':  ['ed', 'hal', 'gav', 'abe', 'bob', 'jon', 'col', 'ian', 'fred', 'dan']}
b3 = sorted(b1.keys())
b4 = sorted(b2.keys())
def fonk1(b15):
    b5 = dict((v,k) for k,v in b15.items())
    for she, he in b15.items():
        b6 = b2[she]
        b7 = b6[:b6.index(he)]
        b8 = b1[he]
        b9 = b8[:b8.index(she)]
        for b18 in b7:
            b10 = b5[b18]
            b11 = b1[b18]
            if b11.index(b10) > b11.index(she):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (she, b18, he, b10))
                return False
        for b20 in b9:
            b12 = b15[b20]
            b13 = b2[b20]
            if b13.index(b12) > b13.index(he):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (he, b20, she, b12))
                return False
    return True
def fonk2():
    b14 = b3[:]
    b15 = {}
    b16 = copy.deepcopy(b1)
    b17 = copy.deepcopy(b2)
    while b14:
        b18 = b14.pop(0)
        b19 = b16[b18]
        b20 = b19.pop(0)
        b21 = b15.get(b20)
        if not b21:
            b15[b20] = b18
            print("  %s and %s" % (b18, b20))
        else:
            b22 = b17[b20]
            if b22.index(b21) > b22.index(b18):
                b15[b20] = b18
                print("  %s dumped %s for %s" % (b20, b21, b18))
                if b16[b21]:
                    b14.append(b21)
            else:
                if b19:
                    b14.append(b18)
    return b15
print('\nEngagements:')
b15 = fonk2()
print('\nCouples:')
print('  ' + ',\n  '.join('%s is b15 to %s' % couple
                          for couple in sorted(b15.items())))
print()
print('Engagement stability check PASSED'
      if fonk1(b15) else 'Engagement stability check FAILED')
print('\n\nSwapping two fiances to introduce an error')
b15[b4[0]], b15[b4[1]] = b15[b4[1]], b15[b4[0]]
for b20 in b4[:2]:
    print('  %s is now b15 to %s' % (b20, b15[b20]))
print()
print('Engagement stability check PASSED'
      if fonk1(b15) else 'Engagement stability check FAILED')