##=========================================================
"""
    Randomized Selection Algorithm
    ------------------------------
    1. Similar to quick sort, but only one recursive
       call per iteration.

    Running Time : O(n) ... best possible partitioning
                   O(n^2) ... Worst Case
"""
##=========================================================
import random
import copy

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def median(array, p, r):
    centre = (p + r)/2
    a = array[p]
    b = array[r]
    c = array[centre]

    piv = 0

    if (a >= b and a <= c) or (a >= c or a <= b):
        piv = p
    elif (b >= a and b <= c) or (b <= a and b >= c):
        piv = centre
    else:
        piv = r

    return piv

 
   
def partition(array, l, r, pivot):
    swap(array, l, pivot)
    pivot = array[l]
    i = l + 1
    j = l + 1

    while j <= r:
        if array[j] < pivot:
            swap(array, i, j)
            i += 1
        j += 1

    swap(array, i - 1, l)

    return i - 1


    
def random_select(array, begin, end, position):
    if begin < end:
        pivot = median(array, begin, end)
        new_pivot = partition(array, begin, end, pivot)
        if position == new_pivot:
            print "Element found", array[new_pivot]
            return
        if position > new_pivot:
            random_select(array, new_pivot + 1, end, position)
        else:
            random_select(array, begin, new_pivot - 1, position)

if __name__ == "__main__":
    array = [8,9,5,6,1,3,4,2,7,0]
    random_select(array, 0, 9, 5)
