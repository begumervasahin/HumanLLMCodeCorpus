import math
a1 = 0
print "\nPrediction Steps"
print "----------------------------------------"
b1 = input("A: ")
b2 = input ("B: ")
b3 = input("Enter Prior Mean: ")
b4 = input ("Enter Current Mean: ")
b5 = b1*b3+b2*b4
print "Predicted Mean: ", b5
b6 = input("\nE(t-1): ")
b7 = input("A(T/t): ")
b8 = input("Q(t): ")
b9 = b1*b6*b7+b8
print "Predicted Convariance: ",b9
while a1 = =0:
	print "\nUpdate Steps"
	print "----------------------------------------"
	b10 = input("C(T/t): ")
	b11 = input("C/(t): ")
	b12 = input ("Measurment Covariance: ")
	b13 = b9*b10*math.pow((b11*b9*b10+b12),(-1))
	print "Kalman Gain: ", b13
	b14 = input("\nActual Measurement: ")
	b15 = b5+b13*(b14-b11*b5)
	print "Updated Mean: ", b15
	b16 = b9-b13*b11*b9
	print "\nUpdated Covariance: ", b16
	print "\nPrediction Steps"
	print "----------------------------------------"
	b1 = input("A: ")
	b2 = input ("B: ")
	b4 = input ("Enter Current Mean: ")
	b5 = b1*b15+b2*b4
	print "Predicted Mean: ", b5
	b7 = input("\nA(T/t): ")
	b8 = input("Q(t): ")
	b9 = b1*b16*b7+b8
	print "Predicted Convariance: ",b9