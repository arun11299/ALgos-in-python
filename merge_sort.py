"""
                       Merge Sort
                       ----------
    Running Time : 6n(log n + 1) = 6nlogn + 6

    Merge sort recursive tree :
            root
            / \
           /   \
        sub_1  sub_2     (Level - 1, Number of sub func = 2 ^ (level(1)))
        /  \    / \       (Size of arra at each level = n/2^(level number))
       /    \  /   \

    Therefore, at any stage, running time is = 2^j * 6(n/(2^j)) = 6n

    Number of recusrsion levels = logn + 1 since array gets divided by
    half at each stage.

    Therefore, total running time = 6n(logn + 1)
"""
#array = [11,10,9,8,7,6,5,4,3,2,1]

array = []

def merge(low, mid, high):
    global array
    i = low
    k = low
    j = mid + 1
    temp_arr = list(xrange(100))
    """
    for i in range (11):
        temp_arr.append(0)
    """ 
    ind = low

    while((i <= mid) and (j <= high)):
        if array[i] <= array[j]:
            temp_arr[ind] = array[i]
            i = i + 1
        else:
            temp_arr[ind] = array[j]
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

        

def merge_sort(low, high):
    global array
    if low < high:
        mid = (low + high)/2
        merge_sort(low, mid)
        merge_sort(mid + 1, high)
        merge(low, mid, high)
        


if __name__ == "__main__":
    global array
    
    fd = open("IntegerArray.txt",'r')
    data = fd.readlines()
    num_of_data = len(data) - 1
    print "Number of dat : " + str(num_of_data)
    for line in data:
        num = int(line.strip('\r\n'))
        array.append(num)
    for elem in array:
        print elem
    
    merge_sort(0,num_of_data)

    for elem in array:
        print elem
