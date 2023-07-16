# implement bubble sort
def bubbleSort(arr):
    n = len(arr)
    for k in range(0, n):
        for j in range(0, n-k-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [44,55,12,42,94,18,6,67]

print("Before sorting : {}".format(arr))
bubbleSort(arr)
print("After sorting : {}".format(arr))