if __name__ == '__main__':
    llist = LinkedList()
    print("Menu")
    print("1)Add element in the front")
    print("2)Add element at the end")
    print("3)Insert at specific position")
    print("4)Delete an element")
    print("5)Display")
    print("6)Quit")
    while True:
        inp = int(input("\nChoose an option: "))
        match inp:
            case 1:
                data = int(input("Enter the data to add in the front: "))
                llist.add_front(data)
            case 2:
                data = int(input("Enter the data to add at the end: "))
                llist.add_last(data)
            case 3:
                data = int(input("Enter the data to insert: "))
                pos = int(input("enter the position to insert: "))
                llist.add_pos(pos, data)
            case 4:
                key = int(input("Enter the value to delete: "))
                llist.delete(key)
            case 5:
                llist.display()
            case 6:
                quit()
            case _:
                print("Enter a valid option")
