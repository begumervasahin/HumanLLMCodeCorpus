from pyspark import SparkContext
sc = SparkContext("local", "Simple App")
def cache_RDD(file_path):
    data = sc.textFile(file_path)
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
        return find_kth_element(dataRDD, k)
    else:
        rez1 = find_kth_element(dataRDD, k)
        rez2 = find_kth_element(dataRDD, k - 1)
        return (rez1 + rez2) / 2
def find_kth_element(dataRDD, k):
    pivot = dataRDD.takeSample(False, 1, seed=0)[0]
    rdd_smaller = dataRDD.filter(lambda x: x < pivot)
    rdd_greater = dataRDD.filter(lambda x: x > pivot)
    if k == (rdd_smaller.count() + 1):
        return pivot
    elif k <= (rdd_smaller.count()):
        return find_kth_element(rdd_smaller, k)
    else:
        return find_kth_element(rdd_greater, k - (rdd_smaller.count() + 1))
cached_RDD = cache_RDD('/Users/Gur/Desktop/data-1.txt')
print("The average of the data set is", calculate_avg(cached_RDD))
print("The minimum of the data set is", calc_minimum(cached_RDD))
print("The maximum of the data set is", maximum(cached_RDD))
print("The variance of the data set is", calc_val(cached_RDD))
print("Median is equal to", find_median(cached_RDD))
sc.stop()