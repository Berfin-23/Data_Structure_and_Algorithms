class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top == None:
            print("Stack Underflow")
        else:
            print(f"The data {self.top.data} is popped")
            self.top = self.top.next

    def peek(self):
        if self.top == None:
            print("Stack is empty")
        else:
            print(f"The top value is {self.top.data}")

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    stack = Stack()
    print("\nMenu")
    print("1)Push")
    print("2)Pop")
    print("3)Peek")
    print("4)Display")
    print("5)Exit")
    while True:
        choice = int(input("\nEnter your choice: "))
        match choice:
            case 1:
                data = int(input("Enter a value to push: "))
                stack.push(data)
            case 2:
                stack.pop()
            case 3:
                stack.peek()
            case 4:
                stack.display()
            case 5:
                print("Quitting")
                quit()
            case _:
                print("Enter a valid option")
