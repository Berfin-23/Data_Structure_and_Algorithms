def partition(arr, start, end):
    pIndex = start
    pivot = arr[end]

    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1

    arr[end], arr[pIndex] = arr[pIndex], arr[end]
    return pIndex


def quickSort(arr, start, end):
    if start < end:
        pIndex = partition(arr, start, end)
        quickSort(arr, start, pIndex - 1)
        quickSort(arr, pIndex + 1, end)
    return arr


lst = [98, 45, 100, 99, 8, 7, 23, 18]
result = quickSort(lst, 0, len(lst)-1)
print(f"Sorted array: {result}")