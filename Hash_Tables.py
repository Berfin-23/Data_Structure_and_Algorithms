# Hashing Function to return key for every value.
def Hashing(keyvalue):
    return keyvalue % len(HashTable)


# Insert Function to add values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)


# Search Function to find a value in the hash table
def search(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    if value in Hashtable[hash_key]:
        print(f"{value} found at key {keyvalue}")
    else:
        print(f"{value} not found in the hash table")


# Delete Function to remove a value from the hash table
def delete(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    if value in Hashtable[hash_key]:
        Hashtable[hash_key].remove(value)
        print(f"{value} deleted from key {keyvalue}")
    else:
        print(f"{value} not found in the hash table")


# Display Function to show the contents of the hash table
def display_hash(hashTable):
    for i in range(len(hashTable)):
        if len(hashTable[i]) > 0:
            print(f"Key {i}: ", end="")
            for j in hashTable[i]:
                print(f"-->{j}", end=" ")
            print()


# Menu-Driven Code
if __name__ == "__main__":
    HashTable = [[] for _ in range(10)]
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
                key = int(input("Enter key: "))
                value = input("Enter value: ")
                insert(HashTable, key, value)
            case 2:
                key = int(input("Enter key: "))
                value = input("Enter value to search: ")
                search(HashTable, key, value)
            case 3:
                key = int(input("Enter key: "))
                value = input("Enter value to delete: ")
                delete(HashTable, key, value)
            case 4:
                display_hash(HashTable)
            case 5:
                break
            case _:
                print("Invalid choice. Please try again.")
