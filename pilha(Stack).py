class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("The stack is empty.")
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("The stack is empty.")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    stack = Stack()
    stack.push(15)
    stack.push(22)
    stack.push(35)
    print(f"Stack : {stack}")