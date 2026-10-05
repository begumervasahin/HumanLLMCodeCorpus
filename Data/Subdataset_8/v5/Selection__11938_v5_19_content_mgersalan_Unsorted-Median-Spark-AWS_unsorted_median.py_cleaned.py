from pyspark import SparkContext
def cache_RDD(file_name, sc):
    data = sc.textFile(file_name)
    dataRDD = data.map(lambda s: float(s))
    dataRDD.cache()
    return dataRDD
def calculate_avg(dataRDD):
    myAvg = dataRDD.sum() / dataRDD.count()
    return myAvg
def calc_minimum(dataRDD):
    min_value = dataRDD.min()
    return min_value
def maximum(dataRDD):
    max_value = dataRDD.max()
    return max_value
def calc_val(dataRDD):
    variance = dataRDD.variance()
    return variance
def find_median(dataRDD):
    n = dataRDD.count()
    k = round(n / 2) + 1
    if n % 2 != 0:
        rez = find_kth_element(dataRDD, k)
        return rez
    else:
        rez1 = find_kth_element(dataRDD, k)
        rez2 = find_kth_element(dataRDD, k - 1)
        rez = (rez1 + rez2) / 2
        return rez
def find_kth_element(Set, k):
    pivot = Set.takeSample(False, 1, seed=0)[0]
    rdd_smaller = Set.filter(lambda x: x < pivot)
    rdd_greater = Set.filter(lambda x: x > pivot)
    if k == (rdd_smaller.count() + 1):
        return pivot
    if k <= (rdd_smaller.count()):
        val = find_kth_element(rdd_smaller, k)
        return val
    if k > (rdd_smaller.count() + 1):
        val = find_kth_element(rdd_greater, k - (rdd_smaller.count() + 1))
        return val
sc = SparkContext()
cached_RDD = cache_RDD('/Users/Gur/Desktop/data-1.txt', sc)
myAvg = calculate_avg(cached_RDD)
print("The average of the data set is", myAvg)
myMin = calc_minimum(cached_RDD)
print("The minimum of the data set is", myMin)
myMax = maximum(cached_RDD)
print("The maximum of the data set is", myMax)
myVar = calc_val(cached_RDD)
print("The variance of the data set is", myVar)
median = find_median(cached_RDD)
print("The median is equal to", median)