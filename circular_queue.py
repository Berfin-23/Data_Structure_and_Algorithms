class Circular_Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def display(self):
        print(self.queue)

    def enqueue(self):
        if (self.rear + 1) % self.size == self.front:
            print("The queue is full")
        else:
            value = int(input("Enter a value to enqueue: "))
            self.rear = (self.rear + 1) % self.size
            if self.front == -1:
                self.front= 0
            self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            self.queue[self.front] = None
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size

size = int(input("Enter the size of the Circular Queue: "))
queue = Circular_Queue(size)
print("Menu")
print("1) Enqueue")
print("2) Dequeue")
print("3) Display")
print("4) Quit")
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
