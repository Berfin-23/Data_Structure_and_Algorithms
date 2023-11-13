def insertionSort(arr, size):
    for i in range(size):
        value = arr[i]
        index = i
        while index > 0 and arr[index - 1] > value:
            arr[index] = arr[index - 1]
            index -= 1
        arr[index] = value
    return arr


lst = [98, 45, 100, 99, 8, 7, 23, 18]
result = insertionSort(lst, len(lst))
print(f"Sorted array: {result}")