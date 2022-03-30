# Import Library
from pyspark.context import SparkContext
import sys

# When the file is about to be executed in terminal
if __name__ == "__main__":
    sc = SparkContext().getOrCreate()
    income_rdd = sc.textFile(sys.argv[1], 32)
    reduced_rdd = income_rdd.map(lambda x: (int(x), 1)).reduceByKey(lambda a, b: a+b).sortByKey()
    distinct = reduced_rdd.count()
    mode = reduced_rdd.max(lambda x: x[1])[0]
    med_loc = income_rdd.count()/2  # index number for the location of the median

    median = 0
    summ = 0
    c = 0
    lst = reduced_rdd.collect()  # All the elements
    while med_loc > summ:
        median = lst[c][0]
        summ += lst[c][1]
        c += 1

    count_10_rdd = reduced_rdd.map(lambda x: (len(str(x[0]))-1, x[1])).reduceByKey(lambda a,b: a+b)
    count_10 = count_10_rdd.collect()
    
    f = open('a2_p1_CSE545sp22_Park_111786264_OUTPUT.txt', 'w')
    f.write("*****OUTPUT*****\n\n")
    f.write("The Number of Distinct Values: {}\n".format(distinct))
    f.write("Median: {}\n".format(median))
    f.write("Mode: {}\n\n".format(mode))
    f.write("*****Count Per 10 Powers*****\n\n")
    for (k, v) in count_10:
        f.write("10 ** {}: {}\n".format(k, v))

    f.close()  # Closing the file
    
        


