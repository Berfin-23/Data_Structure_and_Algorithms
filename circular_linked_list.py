class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.head.next = self.head
        else:
            current = self.head
            while self.head.next:
                current = current.next
            current.next = newNode
            newNode.next = self.head

    def insert_front(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head
            self.head = newNode

    def insert_at(self, data, pos):
        if pos == 0:
            self.insert_front(data)
        else:
            newNode = Node(data)
            current = self.head
            for i in range(pos - 1):
                current = current.next
            newNode.next = current.next
            current.next = newNode

    def delete(self, key):
        if self.head == None:
            print("The list is empty")
            return

        if self.head.data == key:
            if self.head.data == key:
                current = self.head
                while current.next != self.head:
                    current = current.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    current.next = self.head.next
                    self.head = self.head.next
            else:
                prev = None
                current = self.head
                while current.next != self.head:
                    prev = current
                    current = current.next
                    if current.data == key:
                        prev.next = current.next
                        break

    def display(self):
        if self.head == None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                print(f"(back to head: {self.head.data})")
                break


if __name__ == "__main__":
    clist = CircularLinkedList()
    print("\nMenu:")
    print("1)Insert at the beginning")
    print("2)Insert at the end")
    print("3)Insert at a specific position")
    print("4)Delete an element")
    print("5)Display the list")
    print("6)Quit")
    while True:
        choice = int(input("\nEnter a choice: "))
        match choice:
            case 1:
                data = int(input("Enter the value to insert: "))
                clist.insert_front(data)
            case 2:
                data = int(input("Enter the value to insert: "))
                clist.insert_end(data)
            case 3:
                data = int(input("Enter the value to insert: "))
                pos = int(input("Enter the position: "))
                clist.insert_at(data, pos)
            case 4:
                data = int(input("Enter the element to delete: "))
                clist.delete(data)
            case 5:
                clist.display()
            case 6:
                print("Exiting...")
                quit()
            case _:
                print("Invalid choice. Please choose again.")