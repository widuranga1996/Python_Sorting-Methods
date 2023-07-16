def insertionSort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key


arr = [15,6,10,5,3,8]

print("Before sorting : {}".format(arr))
insertionSort(arr)
print("After sorting : {}".format(arr))