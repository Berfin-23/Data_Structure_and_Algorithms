class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def add_last(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
        else:
            lastNode = self.head

        while(lastNode.next):
            lastNode = lastNode.next

        lastNode.next = newNode

    def add_pos(self, pos, data):
        newNode = Node(data)
        temp = self.head
        if pos < 0:
            print("Invalid position")
            return
        elif pos == 0:
            temp.next = self.head
            temp.head = newNode
            return
        num = 0
        while (temp != None) and (num < pos - 1):
            temp = temp.next
            num += 1
        if (temp == None):
            print("Position out of bound")
            return
        newNode.next = temp.next
        temp.next = newNode

    def delete(self, key):
        if self.head.data == key:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next != None:
                if temp.next.data == key:
                    temp.next = temp.next.next
                    break
                else:
                    temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("\n\n\n")


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