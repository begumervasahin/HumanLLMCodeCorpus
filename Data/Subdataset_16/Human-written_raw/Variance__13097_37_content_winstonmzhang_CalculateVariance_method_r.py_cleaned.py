
import statistics
def fonk1(X):
    b1 = float(sum(X))/len(X)
    a1 = 0.0
    for x in X:
        a1 += (x - b1) ** 2
    return (a1/len(X))**0.5
print('Calculate the variance for Method R MOT Edition 3 \
       Sample Sets on page 8')
b2 = [0.924, 0.928, 0.954, 0.957, 0.961, 0.965, 0.972, 0.979, 0.987, 1.373]
print('WZ stddev of b2 is {:15.9f}'.format(fonk1(b2)))
print('WZ variance of b2 is {:15.9f}'.format(fonk1(b2) ** 2))
print('Statistic stddev b2 is {:15.9f}'.format(statistics.stdev(b2)))
print('Population Statistic stddev b2 \
        is {:15.9f}'.format(statistics.pstdev(b2)))
print("Statistic Variance of b2 is \
        {:15.9f}".format(statistics.variance(b2)))
print("Population Statistic Variance of b2 is \
       {:15.9f}".format(statistics.pvariance(b2)))
print('...........................................................')
b3 = [0.091, 0.109, 0.134, 0.136, 0.159, 0.172, 0.185, 0.191, 0.207, 8.616]
print('WZ stddev of b3 is', fonk1(b3))
print('WZ variance of b3 is', fonk1(b3) ** 2)
print('Statistic stddev b3 is', statistics.stdev(b3))
print('Population Statistic stddev b3 is \
       {:15.9f}'.format(statistics.pstdev(b3)))
print("Statistic Variance of b3 is \
         {:15.9f}".format(statistics.variance(b3)))
print("Population Statistic Variance of \
       b3 is {:15.9f}".format(statistics.pvariance(b3)))