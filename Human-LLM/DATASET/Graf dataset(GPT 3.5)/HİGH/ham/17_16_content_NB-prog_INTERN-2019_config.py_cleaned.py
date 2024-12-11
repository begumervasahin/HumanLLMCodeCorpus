'''
b3 : Text file used for training SkipGram.
a1 :  SkipGram is trained on only most frequent a1 vocabularies from the corpus other vocabularies are ignored.
                  To train on all vocabulary provide very high value like 1e12.
a2 :  SkipGram is trained only using first a2 words from the b3. To use all the corpus provide very high value like 1e12.
b4 : If not None, then words are randomly removed from the corpus with the following probability:
                        b1 = 1 - (b4/word_freq)^0.5
a4 : Number of negative words sampled for each context word. It is sampled from following distribution:
                        b2 = (word_freq^0.75)/(sum(word_freq^0.75))
b5: If true, then SkipGram continues training from the previous state.
a8: Number of vocabulary to plot in plot.py.
'''
b3 = 'corpus.txt'
a1 = 50000
a2 = 1e12
b4 = None
a3 = 50
a4 = 20
a5 = 3
a6 = 256
a7 = 5
b5 = False
a8 = 1000