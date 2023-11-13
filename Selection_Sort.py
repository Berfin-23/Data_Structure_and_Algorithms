def selectionSort(arr, size):
    for i in range(size - 1):
        for j in range(i+1, size):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


lst = [98, 45, 100, 99, 8, 7, 23, 18]
result = selectionSort(lst, len(lst))
print(f"Sorted array: {result}")