from collections import deque

class Stack:
    """ A Last In First Out (LIFO) Data Structure.

    Using the Dequeue from collections to implement this.

    """
    def __init__(self):
        self.elements = deque()

    def push(self, data):
        self.elements.append(data)
        return data

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def is_empty(self):
        return len(self.elements) == 0

if __name__ == '__main__':
    help(Stack)