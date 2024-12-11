import gaussianBayes
import multi
import sys
print("\nmultinomial with bag of words")
print("-"*20)
b1 = multi.MN(sys.argv[1],sys.argv[2])
b1.predict(sys.argv[3],sys.argv[4])
print("\ngaussian with bag of words")
print("-"*20)
b2 = gaussianBayes.GN("bag",sys.argv[1],sys.argv[2])
b2.predict(sys.argv[3],sys.argv[4],"bag")
print("\ngaussian with tfidf")
print("-"*20)
b3 = gaussianBayes.GN("tf",sys.argv[1],sys.argv[2])
b3.predict(sys.argv[3],sys.argv[4],"tf")