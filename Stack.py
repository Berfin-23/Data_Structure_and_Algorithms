class Stack:
    def __init__(self, size):
        self.stack = [None] * size #creates a list for the size entered in the line 40
        self.top = -1 #initial top value of the stack
        self.size = size

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def isFull(self):
        if self.top == self.size - 1:
            return True
        return False

    def push(self, data):
        if self.isFull():
            print("Stack overflow")
        else:
            print(f"The data {data} is pushed")
            self.top = self.top + 1
            self.stack[self.top] = data

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
        else:
            self.stack[self.top] = None
            self.top = self.top - 1
            print(f"The data {self.stack[self.top]} is popped")

    def peek(self):
        print(f"The value at the top is {self.stack[self.top]}")

    def display(self):
        print(self.stack)


size = int(input("Enter the size of the stack: "))
stack = Stack(size)
print("Menu")
print("1)Push")
print("2)Pop")
print("3)Peek")
print("4)Display")
print("5)Quit")
while True:
    choice = int(input("\nEnter you choice: "))
    #match case is only supported in Python 3.10 or later
    match choice:
        case 1:
            data = int(input("Enter the data to push: "))
            stack.push(data)
        case 2:
            stack.pop()
        case 3:
            stack.peek()
        case 4:
            stack.display()
        case 5:
            print("Quitting...")
            quit()
        case _:
            print("Enter a valid choice")
