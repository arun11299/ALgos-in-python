"""
Quick Sort Implementation
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

def median(left, right):
    global array
    
    centre = (left + right)/2
    
    if array[left] > array[centre]:
        swap(left, centre)
    if array[left] > array[right]:
        swap(left, right)
    if array[centre] > array[right]:
        swap(centre, right)
        
    swap(centre, right - 1)
    return array[right - 1]
    

def quickSort(begin, end):
    global array
    global comparison

    #mid = (begin + end)/2
    #pivot = array[mid]
    #pivot = array[random.randint(begin, end)]
    pivot = median(begin, end)

    #swap(begin, end)
    #pivot = array[end]

        
    i = begin
    j = end

    while i<= j:
        while array[i] < pivot:
            #comparison += 1
            i += 1
        while array[j] > pivot:
            #comparison += 1
            j -= 1
            
        if i <= j:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp

            i += 1
            j -= 1

    if j > begin:
        comparison += j - begin
        quickSort(begin, j)
    if i < end:
        comparison += end - i
        quickSort(i, end)
     

if __name__ == "__main__":

    fd = open("QuickSort.txt", "r")
    data = fd.readlines()
    num_of_data = len(data) - 1

    for line in data:
        num = int(line.strip('\r\n'))
        array.append(num)
        
    quickSort(0, num_of_data)
    for elem in array:
        print elem

    print comparison
