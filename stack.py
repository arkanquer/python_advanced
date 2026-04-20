class Stack:
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        #return self._items[len(self._items) - 1]
        return self._items[- 1]

    def size(self):
        return len(self._items)

    def get_from_stack(self, value):
        temp_stack = Stack()

        found = False

        while not stack.isEmpty():
            item = stack.pop()

            if item == value:
                found = True

            temp_stack.push(item)

        while not temp_stack.isEmpty():
            stack.push(temp_stack.pop())

        if found:
            return value
        else:
            raise ValueError


    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


def task1(value):
    stack = Stack()
    for i in value:
        stack.push(i)
    while not stack.isEmpty():
        print(stack.peek(), end="")
        stack.pop()
print("task1: ", end="")
task1("hello")

def task2(value):
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = Stack()
    for i in value:
        if i in "([{":
            stack.push(i)
        if i in ")]}":
            if stack.isEmpty():
                return False
            if stack.peek() != pairs[i]:
                return False
            stack.pop()
    return stack.isEmpty()
print("\ntask2:", task2("{}"))

stack = Stack()
for i in "hello":
    stack.push(i)
print(stack.get_from_stack("h"))