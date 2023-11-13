class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.rear:
            print("The queue is full")
        else:
            self.rear = (self.rear + 1) % self.size
            if self.front == -1:
                self.front = 0
            self.queue[self.rear] = data
            print(f"The data {data} is enqueued")

    def dequeue(self):
        if self.front == -1:
            print("The queue is empty")
        else:
            print(f"The data {self.queue[self.front]} is dequed")
            self.queue[self.front] = None
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size

    def display(self):
        print(self.queue)


size = int(input("Enter the size of the queue: "))
queue = Queue(size)
print("Menu")
print("1)Enqueue")
print("2)Dequeue")
print("3)Display")
print("4)Quit")
while True:
    choice = int(input("\nEnter your choice: "))
    match choice:
        case 1:
            data = int(input("Enter the data to enqueue: "))
            queue.enqueue(data)
        case 2:
            queue.dequeue()
        case 3:
            queue.display()
        case 4:
            print("Exiting...")
            quit()
        case _:
            print("Enter a valid choice")
