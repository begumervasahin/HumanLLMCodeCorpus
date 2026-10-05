import copy
guyprefers = {
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
galprefers = {
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
guys = sorted(guyprefers.keys())
gals = sorted(galprefers.keys())
def check_stability(engaged):
    inverse_engaged = {v: k for k, v in engaged.items()}
    for she, he in engaged.items():
        she_likes = galprefers[she]
        she_likes_better = she_likes[:she_likes.index(he)]
        he_likes = guyprefers[he]
        he_likes_better = he_likes[:he_likes.index(she)]
        for guy in she_likes_better:
            guy_s_girl = inverse_engaged[guy]
            guy_likes = guyprefers[guy]
            if guy_likes.index(guy_s_girl) > guy_likes.index(she):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (she, guy, he, guy_s_girl))
                return False
        for gal in he_likes_better:
            gal_s_guy = engaged[gal]
            gal_likes = galprefers[gal]
            if gal_likes.index(gal_s_guy) > gal_likes.index(he):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (he, gal, she, gal_s_guy))
                return False
    return True
def matchmaker():
    guys_free = guys[:]
    engaged = {}
    guyprefers_copy = copy.deepcopy(guyprefers)
    galprefers_copy = copy.deepcopy(galprefers)
    while guys_free:
        guy = guys_free.pop(0)
        guys_list = guyprefers_copy[guy]
        gal = guys_list.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            engaged[gal] = guy
            print("  %s and %s" % (guy, gal))
        else:
            gals_list = galprefers_copy[gal]
            if gals_list.index(fiance) > gals_list.index(guy):
                engaged[gal] = guy
                print("  %s dumped %s for %s" % (gal, fiance, guy))
                if guyprefers_copy[fiance]:
                    guys_free.append(fiance)
            else:
                if guys_list:
                    guys_free.append(guy)
    return engaged
print('\nEngagements:')
engaged = matchmaker()
print('\nCouples:')
print('  ' + ',\n  '.join('%s is engaged to %s' % couple
                           for couple in sorted(engaged.items())))
print()
print('Engagement stability check PASSED'
      if check_stability(engaged) else 'Engagement stability check FAILED')
print('\n\nSwapping two fiances to introduce an error')
engaged[gals[0]], engaged[gals[1]] = engaged[gals[1]], engaged[gals[0]]
for gal in gals[:2]:
    print('  %s is now engaged to %s' % (gal, engaged[gal]))
print()
print('Engagement stability check PASSED'
      if check_stability(engaged) else 'Engagement stability check FAILED')