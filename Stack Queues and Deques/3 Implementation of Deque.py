'''

Pronounced as - Deck

1. Double ended queue, ordered collection of items similar to Queue
2. It has two ends front and rear
3. What makes a deque different is the unrestricted nature of adding and removing items
4. New items can be added at either front or the rear
5. Likewise, exiting items can be removed from either end


'''

class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
d.add_front('hello')
d.add_rear('World')
print(d.remove_front()+' '+d.remove_rear())
