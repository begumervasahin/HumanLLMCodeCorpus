import distsim
b1 = distsim.load_word2vec("nyt_word2vec.4k")
print("Word 1 is::::america")
for i, (word, score) in enumerate(distsim.show_nearest(b1, b1['america'],set(['america']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i, word, score))
print("--------------------")
print("Word 2 is::::years")
for i, (word, score) in enumerate(distsim.show_nearest(b1, b1['years'],set(['years']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i, word, score))
print("--------------------")
print("Word 3 is::::great")
for i, (word, score) in enumerate(distsim.show_nearest(b1, b1['great'],set(['great']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i, word, score))
print("--------------------")
print("Word 4 is::::run")
for i, (word, score) in enumerate(distsim.show_nearest(b1, b1['run'],set(['run']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i, word, score))
print("--------------------")
print("Word 5 is::::between")
for i, (word, score) in enumerate(distsim.show_nearest(b1, b1['between'],set(['between']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i, word, score))
print("--------------------")
print("Word 6 is::::wife")
for i, (word, score) in enumerate(distsim.show_nearest(b1, b1['wife'],set(['wife']),distsim.cossim_dense)):
    print("{}: {} ({})".format(i, word, score))
print("--------------------")