"""
            Counting Split inversions
            -------------------------
        Can be done using "Divide And Conquer Paradigm".
        Thus can be achieved by piggybacking on merge sort.
"""
#array = [1, 20, 6, 4, 5]
array = []

def merge(low, mid, high):
    global array
    i = low
    k = low
    j = mid + 1
    temp_arr = [0,0,0,0,0]
    ind = low

    inv_count = 0
    
    while((i <= mid) and (j <= high)):
        if array[i] <= array[j]:
            temp_arr[ind] = array[i]
            i = i + 1
        else:
            temp_arr[ind] = array[j]
            """
                Right sub array has a smaller element than
                the left sub array, thus there is an inversion
            """
            inv_count = inv_count + (mid - i + 1)
            print "count :: %s"%(str(inv_count))
            j = j + 1
            
        ind = ind + 1

    if i > mid:
        while j <= high:
            temp_arr[ind] = array[j]
            ind = ind  + 1
            j = j + 1
    else:
        while i <= mid:
            temp_arr[ind] = array[i]
            ind = ind + 1
            i = i + 1
               
    while k<= high:
        array[k] = temp_arr[k]
        k = k + 1
        
    return inv_count
        

def merge_sort(low, high):
    global array
    inv_count = 0
    if low < high:
        mid = (low + high)/2
        inv_count = merge_sort(low, mid)
        inv_count = inv_count + merge_sort(mid + 1, high)
        inv_count = inv_count + merge(low, mid, high)

    return inv_count
        


if __name__ == "__main__":
    global array
    fd = open("IntegerArray.txt",'r')
    data = fd.readlines()
    num_of_data = len(data) - 1
    
    for line in data:
        num = int(line.strip('\r\n'))
        array.append(num)
        
    count = merge_sort(0,num_of_data)

    print "Inversion count :: %s"%(str(count))

    for elem in array:
        print elem
