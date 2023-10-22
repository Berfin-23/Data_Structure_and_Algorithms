class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            new_node.prev = temp
            temp.next = new_node

    def insert_at(self, pos, data):
        new_node = Node(data)
        temp = self.head
        i = 1
        while temp and i < pos:
            temp = temp.next
            i += 1
        if temp:
            new_node.next = temp
            new_node.prev = temp.prev
            if temp.prev:
                temp.prev.next = new_node
            temp.prev = new_node
        else:
            print("Index out of bound")

    def delete_front(self):
        if self.head:
            temp = self.head
            if temp.next:
                temp.next.prev = None
                self.head = temp.next
            else:
                self.head = None
        else:
            print("List is empty")

    def delete_last(self):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            if temp.prev:
                temp.prev.next = None
            else:
                self.head = None
        else:
            print("List is empty")

    def delete_at(self, pos):
        if self.head:
            if pos <= 1:
                print("Position should be greater than or equal to 1")
            else:
                temp = self.head
                i = 1
                while temp and i < pos:
                    temp = temp.next
                    i += 1
                if temp:
                    if temp.prev:
                        temp.prev.next = temp.next
                    else:
                        self.head = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                else:
                    print("Index out of bound")
        else:
            print("List is empty")

    def delete_data(self, data):
        if self.head:
            current = self.head
            while current:
                if current.data == data:
                    if current.prev:
                        current.prev.next = current.next
                    else:
                        self.head = current.next
                    if current.next:
                        current.next.prev = current.prev
                    return
                current = current.next
            print("Data not found in the list")
        else:
            print("List is empty")

    def display(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.data, end=" <-> ")
                temp = temp.next
            print("\b\b\b\b-> None")
        else:
            print("List is empty")

    def display_rev(self):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            print(None, end = " -> ")
            while temp:
                print(temp.data, end=" <-> ")
                temp = temp.prev
            print("\b\b\b\b")
        else:
            print("List is empty")

if __name__ == '__main__':
    llist = DoublyLinkedList()
    print("Menu")
    print("1)Add element in the front")
    print("2)Add element at the end")
    print("3)Insert at specific position")
    print("4)Delete at front")
    print("5)Delete at end")
    print("6)Delete at specific position")
    print("7)Delete a specific element")
    print("8)Display")
    print("9)Display in reverse")
    print("10)Exit")
    while True:
        inp = int(input("\nChoose an option: "))
        match inp:
            case 1:
                data = int(input("Enter the data to add in the front: "))
                llist.insert_front(data)
            case 2:
                data = int(input("Enter the data to add at the end: "))
                llist.insert_back(data)
            case 3:
                data = int(input("Enter the data to insert: "))
                pos = int(input("enter the position to insert: "))
                llist.insert_at(pos, data)
            case 4:
                llist.delete_front()
            case 5:
                llist.delete_last()
            case 6:
                pos = int(input("Enter the position to delete: "))
                llist.delete_at(pos)
            case 7:
                data = int(input("Enter the data: "))
                llist.delete_data(data)
            case 8:
                llist.display()
            case 9:
                llist.display_rev()
            case 10:
                print("Exiting...")
            case _:
                print("Enter a valid choice")