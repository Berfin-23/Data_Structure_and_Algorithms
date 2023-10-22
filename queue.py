class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size

    def display(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            print(self.queue)

    def enqueue(self):
        if self.rear == self.size:
            print("The queue is full")
        else:
            value = int(input("Enter a value to enqueue: "))
            self.queue[self.rear] = value
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            self.queue[self.front] = None
            self.front += 1

size = int(input("Enter the size of the Queue: "))
queue = Queue(size)
print("Menu")
print("1)Enqueue")
print("2)Dequeue")
print("3)Display")
print("4)Quit")
while True:
    inp = int(input("\nEnter your option: "))
    match inp:
        case 1:
            queue.enqueue()
        case 2:
            queue.dequeue()
        case 3:
            queue.display()
        case 4:
            print("Quitting")
            quit()
        case _:
            print("Enter a valid option")