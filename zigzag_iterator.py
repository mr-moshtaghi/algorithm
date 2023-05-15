class ZigZag:
    def __init__(self, l1, l2):
        self.queue = [l1, l2]

    def next(self):
        ls = self.queue.pop(0)
        v = ls.pop(0)
        if ls:
            self.queue.append(ls)
        return v

    def has_item(self):
        if self.queue:
            return True


z = ZigZag([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])

while z.has_item():
    print(z.next(), end=" ")
