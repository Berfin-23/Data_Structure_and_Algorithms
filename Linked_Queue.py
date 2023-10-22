class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.front == None and self.rear == None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
        elif self.front == self.rear:
            print(f"The element {self.front.data} is popped")
            self.front = self.rear = None
        else:
            print(f"The element {self.front.data} is popped")
            self.front = self.front.next

    def display(self):
        if self.front == None:
            print("Queue is empty")
        else:
            current = self.front
            while current:
                print(current.data, end = " -> ")
                current = current.next
            print("\b\b\b")

if __name__ == "__main__":
    queue = Queue()
    print("\nMenu")
    print("1)Enqueue")
    print("2)Dequeue")
    print("3)Display")
    print("4)Quit")
    while True:
        choice = int(input("\nEnter your choice: "))
        match choice:
            case 1:
                data = int(input("Enter data to Enqueue: "))
                queue.enqueue(data)
            case 2:
                queue.dequeue()
            case 3:
                queue.display()
            case 4:
                print("Quitting...")
                quit()
            case _:
                print("Invalid choice")
