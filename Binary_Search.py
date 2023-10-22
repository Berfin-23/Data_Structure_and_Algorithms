def binarySearch(arr, key, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    return None


lst = [7, 8, 12, 18, 23, 56, 78, 99, 100, 108]
key = int(input("Enter the number to search: "))
result = binarySearch(lst, key, 0, len(lst) - 1)
if result is not None:
    print(f"The number {key} found at the index {result}")
else:
    print(f"The number {key} is not found")
