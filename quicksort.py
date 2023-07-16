def partition(array, lb, ub):
    pivot = array[lb]
    start = lb + 1
    end = ub

    while True:

        while start <= end and array[start] <= pivot:
            start = start + 1

        while start <= end and array[end] > pivot:
            end = end - 1

        if start < end:
            array[start], array[end] = array[end], array[start]
        else:
            break

    array[lb], array[end] = array[end], array[lb]
    return end

def quickSort(array, start, end):
    if start >= end:
        return

    k = partition(array, start, end)
    quickSort(array, start, k-1)
    quickSort(array, k+1, end)


data = [25,57,48,37,12,92,86,33]
print("Before Sorting : {}".format(data))

lb = 0
up = len(data)-1
quickSort(data, lb, up)
print("After Sorting : {}".format(data))