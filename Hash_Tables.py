def hashing(key_value):
    return key_value % len(hash_table)

def insert(hash_table, key_value, data):
    hash_key = hashing(key_value)
    hash_table[hash_key].append(data)


def search(hash_table, key_value, data):
    hash_key =  hashing(key_value)
    if data in hash_table[hash_key]:
        print(f"The data {data} is found at the key {key_value}")
    else:
        print(f"The data {data} is not found at the key")


def delete(hash_table, key_value, data):
    hash_key = hashing(key_value)
    if data in hash_table[hash_key]:
        hash_table[hash_key].remove(data)
        print(f"The data {data} is deleted")
    else:
        print(f"The data {data} is not found")


def display(hash_table):
    for i in range(len(hash_table)):
        if len(hash_table[i]) > 0:
            print(f"key {i}: ", end ="")
            for j in hash_table[i]:
                print(f"--> {j}", end = " ")
            print()

if __name__ == "__main__":
    hash_table = [[] for _ in range(10)]
    print("\nMenu:")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    while True:
        choice = int(input("\nEnter your choice: "))
        match choice:
            case 1:
                key_value = int(input("Enter key: "))
                data = input("Enter value: ")
                insert(hash_table, key_value, data)
            case 2:
                key_value = int(input("Enter key: "))
                data = input("Enter value to search: ")
                search(hash_table, key_value, data)
            case 3:
                key_value = int(input("Enter key: "))
                data = input("Enter value to delete: ")
                delete(hash_table, key_value, data)
            case 4:
                display(hash_table)
            case 5:
                break
            case _:
                print("Invalid choice. Please try again.")
