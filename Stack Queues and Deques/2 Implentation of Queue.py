'''

1. Addition occurs at one end - rear
2. Removal occurs at other end - front
3. First In First Out -- First Come First Served -- FIFO
Eg: The first person in the for Tea is also the first person
    to get serviced/helped

4. Enqueue - When we add a new item to the rear to the Queue
5. Dequeue - When we remove the front item from the Queue

'''


class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(2)

print(q.dequeue())
