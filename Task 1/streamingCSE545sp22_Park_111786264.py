##########################################################################
## streamingCSE545sp22_lastname_id.py  v1
## 
## Template code for assignment 1 part 1. 
## Do not edit anywhere except blocks where a #[TODO]# appears
##
## Student Name: Haein Park
## Student ID: 111786264


import sys
from pprint import pprint
from random import random
from collections import deque
from sys import getsizeof
import resource
import math

##########################################################################
##########################################################################
# Methods: implement the methods of the assignment below.  
#
# Each method gets 1 100 element array for holding ints of floats. 
# This array is called memory1a, memory1b, or memory1c
# You may not store anything else outside the scope of the method.
# "current memory size" printed by main should not exceed 8,000.

MEMORY_SIZE = 100 #do not edit

memory1a =  deque([None] * MEMORY_SIZE, maxlen=MEMORY_SIZE) #do not edit

# Calculating the mean values
def mean(l, start, end):
    sum = 0
    for i in range(start, end):
        sum += l[i]
    return sum/(end - start)

def median(l):
    l.sort()
    return l[len(l)//2]

def trailZeros(bit):
    c = 0
    while(c < len(bit) and bit[-(c+1)] == "0"):
        c += 1
    return c

def task1ADistinctValues(element, returnResult = True):
    #[TODO]#
    #procss the element you may only use memory1a, storing at most 100 
    
    ##### Each group of hash functions consists of 3 hash functions
    ##### Here, we assume the true number of distinct elements in our stream is 2^64.
    ##### For all of my hash functions, they will have the form of (a*x + b) % 64
    ##### where a and b are odd numbers.
    ##### bin()[2:] is to get rid of the prefix "0b"

    # Group 1: b = a + 2
    a = 1
    b = a + 2
    for i in range(20):
        if memory1a[i] == None:
            memory1a.append((lambda e: 2 ** trailZeros(bin((a*e + b)%64)[2:])) (element))
        else:
            memory1a.append(max(memory1a[i], (lambda e: 2 ** trailZeros(bin((a*e + b)%64)[2:]))(element)))
        a = b
        b += 2

    # Group 2: b = a + 4
    a = 1
    b = a + 4
    for i in range(20, 40):
        if memory1a[i] == None:
            memory1a.append((lambda e: 2 ** trailZeros(bin((a*e + b)%64)[2:])) (element))
        else:
            memory1a.append(max(memory1a[i], (lambda e: 2 ** trailZeros(bin((a*e + b)%64)[2:]))(element)))
        a = b
        b += 4

    # Group 3: b = a + 6
    a = 3
    b = a + 6
    for i in range(40, 60):
        if memory1a[i] == None:
            memory1a.append((lambda e: 2 ** trailZeros(bin((a*e + b)%64)[2:])) (element))
        else:
            memory1a.append(max(memory1a[i], (lambda e: 2 ** trailZeros(bin((a*e + b)%64)[2:]))(element)))
        a = b
        b += 6

    # Group 4: b = a + 8
    a = 5
    b = a + 8
    for i in range(60, 80):
        if memory1a[i] == None:
            memory1a.append((lambda e: 2 ** trailZeros(bin((a*e + b)%64)[2:])) (element))
        else:
            memory1a.append(max(memory1a[i], (lambda e: 2 ** trailZeros(bin((a*e + b)%64)[2:]))(element)))
        a = b
        b += 8

    # Group 5: b = a + 10
    a = 1
    b = a + 10
    for i in range(80, 100):
        if memory1a[i] == None:
            memory1a.append((lambda e: 2 ** trailZeros(bin((a*e + b)%64)[2:])) (element))
        else:
            memory1a.append(max(memory1a[i], (lambda e: 2 ** trailZeros(bin((a*e + b)%64)[2:]))(element)))
        a = b
        b += 10


    if returnResult: #when the stream is requesting the current result
        mean1 = mean(memory1a, 0, 20)
        mean2 = mean(memory1a, 20, 40)
        mean3 = mean(memory1a, 40, 60)
        mean4 = mean(memory1a, 60, 80)
        mean5 = mean(memory1a, 80, 100)
        
        Median = median([mean1, mean2, mean3, mean4, mean5])
        
        result = Median
        #[TODO]#
        #any additional processing to return the result at this point
        return result
    else: #no need to return a result
        pass


memory1b =  deque([None] * MEMORY_SIZE, maxlen=MEMORY_SIZE) #do not edit

def task1BMedian(element, returnResult = True):
    #[TODO]#
    #procss the element
    
    # Index 0: counter
    # Index 1: summation of the natural logged values

    if memory1b[0] == None and memory1b[1] == None:
        memory1b[0] = 1
        memory1b[1] = math.log(element)
    else:
        memory1b[0] += 1
        memory1b[1] += math.log(element)
    
    if returnResult: #when the stream is requesting the current result
        result = 1/(0.5**(1/(memory1b[0]/memory1b[1])))
        #[TODO]#
        #any additional processing to return the result at this point
        return result
    else: #no need to return a result
        pass
    

memory1c =  deque([None] * MEMORY_SIZE, maxlen=MEMORY_SIZE) #do not edit

def task1CMostFreqValue(element, returnResult = True):
    #[TODO]#
    #procss the element
    
    if returnResult: #when the stream is requesting the current result
        result = 0
        #[TODO]#
        #any additional processing to return the result at this point
        return result
    else: #no need to return a result
        pass


##########################################################################
##########################################################################
# MAIN: the code below setups up the stream and calls your methods
# Printouts of the results returned will be done every so often
# DO NOT EDIT BELOW

def getMemorySize(l): #returns sum of all element sizes
    return sum([getsizeof(e) for e in l])+getsizeof(l)

if __name__ == "__main__": #[Uncomment peices to test]
    
    print("\n\nTESTING YOUR CODE\n")
    
    ###################
    ## The main stream loop: 
    print("\n\n*************************\n Beginning stream input \n*************************\n")
    filename = sys.argv[1]#the data file to read into a stream
    printLines = frozenset([10**i for i in range(1, 20)]) #stores lines to print
    peakMem = 0 #tracks peak memory usage
    
    with open(filename, 'r') as infile:
        i = 0#keeps track of lines read
        for line in infile:
        
            #remove \n and convert to int
            element = int(line.strip())
            i += 1

            #call tasks         
            if i in printLines: #print status at this point: 
                result1a = task1ADistinctValues(element, returnResult=True)
                result1b = task1BMedian(element, returnResult=True)
                result1c = task1CMostFreqValue(element, returnResult=True)
                
                print(" Result at stream element # %d:" % i)
                print("   1A:     Distinct values: %d" % int(result1a))
                print("   1B:              Median: %.2f" % float(result1b))
                print("   1C: Most frequent value: %d" % int(result1c))
                print(" [current memory sizes: A: %d, B: %d, C: %d]\n" % \
                    (getMemorySize(memory1a), getMemorySize(memory1b), getMemorySize(memory1c)))
                  
            else: #just pass for stream processing
                result1a = task1ADistinctValues(element, False)
                result1b = task1BMedian(element, False)
                result1c = task1CMostFreqValue(element, False)
                
            memUsage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            if memUsage > peakMem: peakMem = memUsage
        
    print("\n*******************************\n       Stream Terminated \n*******************************")
    print("(peak memory usage was: ", peakMem, ")")
