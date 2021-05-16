'''

1. Ordered Collection
2. Addition and Removal at same end
3. End is commonly referred as "Top"
4. Opposite ot "Top" is "base" or "bottom"
5. Last In First Out - LIFO

Eg: Stack of books on Table

'''


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


s = Stack()
s.push(1)
s.push('two')
print(s.peek())
s.push(True)
print(s.size())
s.pop()

