# FIFO


class Queue:

    def __init__(self):
        self.queue = []

    def __repr__(self):
        return f"Queue: {self.queue!r}, size :{self.size_queue()}"

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)


def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Size: {queue.size_queue()}")
    print(f"Dequeue item: {queue.dequeue()}")
    print(f"Size: {queue.size_queue()}")
    print(f"Dequeue item: {queue.dequeue()}")
    print(f"Dequeue item: {queue.dequeue()}")
    print(f"Dequeue item: {queue.dequeue()}")
    print(f"Dequeue item: {queue.dequeue()}")
    print(f"Size: {queue.size_queue()}")


if __name__ == '__main__':
    main()
