class Queue:
    def __init__(self, *args):
        self.queue = [*args]
        self.index = 0

    def enqueue(self, *args):
        for arg in args:
            self.queue.append(arg)

    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]

    def isempty(self) -> bool:
        return len(self.queue) == 0

    def __repr__(self):
        return "Queue " + "".join(str(self.queue))

    def __str__(self):
        return "".join(str(self.queue))

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.queue[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

    def __getitem__(self, value):
        return self.queue[value]

queue = Queue(1, 2, 3)
queue.enqueue(72, "hello world")
