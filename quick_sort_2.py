"""
Quick Sort Implementation
1. Quick Sort with pivot as first element of array.
2. Quick Sort with pivot as last element of array.
3. Quick Sort with pivot as median of (first, centre, last) element of array.


Arun Muralidharan
"""
import random
#array = [1,2,3,4,5,6,7,8,9]
array = []
comparison = 0

def swap(a, b):
    global array
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def median(p, r): ## Computes the median, as per sedgewick gives
                  ## gives better performance in average case analysis.
    global array

    centre = (p + r)/2
    a = array[p]
    b = array[centre]
    c = array[r]
    piv = 0
 
    if (a >= b and a <= c) or (a >= c and a <= b):
        piv = p
    elif (b >= a and b <= c) or (b>= c and b <= a):
        piv = centre
    else:
        piv = r

    return piv

"""
Partitioning Algorithm :
-----------------------
Assume pivot as the first element of the array
[If not, swap pivot <-> 1st element as preprocessing step]

High level Idea :
-----------------------------------
| P |  <p  |  >p  |                |
-----------------------------------
           ^(i)   ^(j)
    <-------------><-------------->
     Partitioned     unpartitioned(elements we havent lokked at or iterated through till now)

i : points to the partion between less than and greater than
j : points to the last element scanned

1. Single scan through array
2. Invariant: everything looked at so far is partioned.
"""

def partition(l,r, pivot):
    global array
    global comparison

    swap(l,pivot)       ## Swap it with the begining value, as the algorithm is easier to analyse,
			## implement for different pivot values.
    pivot = array[l]
    
    i = l + 1
    j = l + 1
    
    while j <= r :
        comparison += 1
        if array[j] > pivot:
                swap(i,j)
                i += 1
        j += 1
   
    temp = array[i-1]
    array[i-1] = array[l]
    array[l] = temp
    
    return i - 1



def quickSort(begin, end):
    global array
    global comparison
    #comparison += end - begin
    
    if begin < end:
        m_pivot = median(begin, end)
        pivot = partition(begin, end, m_pivot)
        quickSort(begin, pivot - 1)
        quickSort(pivot + 1,end)
     

if __name__ == "__main__":
    
    fd = open("QuickSort.txt", "r")
    data = fd.readlines()
    num_of_data = len(data) - 1

    # Load the data into the array
    for line in data:
        num = int(line.strip('\r\n'))
        array.append(num)

    quickSort(0, num_of_data)
    
    for elem in array:
        print elem

    print comparison
    
