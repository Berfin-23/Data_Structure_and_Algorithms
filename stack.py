class stack:
    def __init__(self, size):
        self.arr = [None] * size
        self.top = -1
        self.size = size

    def display(self):
        print(self.arr)

    def push(self, value):
        if self.top == self.size -1:
            print("Stack is full")
        else:
            self.top = self.top + 1
            self.arr[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            self.arr[self.top] = None
            self.top = self.top - 1

    def peek(self):
        print(self.arr[self.top])


size = int(input("Enter the size of the stack: "))
Stack = stack(size)
print("Menu:")
print("1)Push an element")
print("2)Display the stack")
print("3)Pop an element")
print("4)Peek")
print("5)Quit")
while True:
    inp = int(input("\nEnter your choice: "))
    match inp:
        case 1:
            val = int(input("Enter a value to push: "))
            Stack.push(val)
        case 2:
            Stack.display()
        case 3:
            Stack.pop()
        case 5:
            print("Quitting")
            quit()
        case 4:
            Stack.peek()
        case _:
            print("Enter a valid option")
