class Queue:
    def __init__(self, size):
        self.queue = [None] * size #Creates a list based in size entered in line 29
        #initial values
        self.front = 0
        self.rear = 0
        self.size = size

    def enqueue(self, data):
        if self.size == self.rear:
            print("The queue is full")
        else:
            self.queue[self.rear] = data
            self.rear += 1
            print(f"The data {data} is enqueued")

    def dequeue(self):
        if self.front == self.rear:
            print("The queue is empty")
        else:
            print(f"The data {self.queue[self.front]} is dequed")
            self.queue[self.front] = None
            self.front += 1

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
    #match case is supported in Python 3.10+
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
