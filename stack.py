class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]


# Testing the stack implementation
if __name__ == "__main__":
    my_stack = Stack()

    print("Is the stack empty?", my_stack.isEmpty())  # Output: True

    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print("Size of the stack:", my_stack.size())  # Output: 3
    print("Is the stack empty?", my_stack.isEmpty())  # Output: False

    print("Top item of the stack:", my_stack.peek())  # Output: 30
    print("Popped item:", my_stack.pop())  # Output: 30

    print("Size of the stack after popping:", my_stack.size())  # Output: 2
