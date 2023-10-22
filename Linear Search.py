def linear_search(arr, key):
    ind = 0
    for i in arr:
        if i == key:
            return ind
        ind += 1
    return None


lst = [45, 7, 10, 3, 8, 99]
key = int(input("Enter the key to search: "))
res = linear_search(lst, key)
if res is not None:
    print(f"The value {key} is found at the index {res}")
else:
    print(f"The value {key} is not found")