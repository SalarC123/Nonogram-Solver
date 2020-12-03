'''
DEPTH FIRST SEARCH (TYPE OF BACKTRACKING ALGORITHM) - CREATE STACK TO IMPLEMENT
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, top = None):
        self.top = Node(top)

    def push(self, num):
        new = Node(num)
        new.next = self.top
        self.top = new

    def pop(self):
        if not self.top:
            return
        elif not self.top.next:
            self.top = None
        else:
            self.top.value = self.top.next.value
            self.top.next = self.top.next.next


    def display(self):
        lst = []
        current = self.top
        while current:
            lst.append(current.value)
            lst.append('-->')
            current = current.next
        lst.append(None)
        return f'{lst}'

# stack = Stack(1)
# stack.push(2)
# stack.push(3)
# print(stack.display())