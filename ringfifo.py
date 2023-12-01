from abc import ABC, abstractmethod

class RingQueue(ABC):
    @abstractmethod
    def push(self, item) -> None:
        pass

    @abstractmethod
    def isEmpty(self) -> bool:
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

class RingQueue1(RingQueue):
    def __init__(self, capacity: int = 8):
        self.capacity = capacity
        self.items = [None for i in range(capacity)]
        self.head = capacity - 1
        self.tail = capacity - 1
 
    def push(self, item):
        if item is None:
            raise ValueError("Cannot use None as a value in ring queue")
        if self.head == self.tail and self.items[self.head] is not None:
            new_array = [None for i in range(self.capacity * 2)]
            start_index = 0 if self.tail + 1 == self.capacity else self.tail + 1
            for i in range(start_index, start_index + self.capacity):
                new_array[i - start_index] = self.items[i - self.capacity]
            self.items = new_array
            self.head = self.capacity - 1
            self.capacity *= 2
            self.tail = self.capacity - 1
        self.items[self.tail] = item
        self.tail = self.capacity - 1 if self.tail == 0 else self.tail - 1
  
    def isEmpty(self) -> bool:
        return self.head == self.tail and self.items[self.head] is None
 
    def pop(self):
        if self.isEmpty():
            raise IndexError("Ring queue is empty")
        value = self.items[self.head]
        self.items[self.head] = None
        self.head = self.capacity - 1 if self.head == 0 else self.head - 1
        return value
  
    def peek(self):
        if self.isEmpty():
            raise IndexError("Ring queue is empty")
        return self.items[self.head]
  
if __name__ == "__main__":
    queue = RingQueue1(4)
    queue.push(30)
    queue.push(100)
    queue.push(40)
    print(queue.peek(), queue.pop(), queue.peek())
    queue.push(140)
    queue.push(70)
    queue.push(-70)
    queue.push(0)
    print(queue.items)
    print(queue.pop())

