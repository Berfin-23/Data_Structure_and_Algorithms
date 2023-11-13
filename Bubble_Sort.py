def bubbleSort(arr, size):
    for i in range(size-1):
        for j in range(size-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[ j + 1], arr[j]
    return arr


lst = [98, 45, 100, 99, 8, 7, 23, 18]
result = bubbleSort(lst, len(lst))
print(f"Sorted array: {result}")