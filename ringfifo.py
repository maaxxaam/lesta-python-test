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
        # None denotes an abscence of an item
        self.items = [None for i in range(capacity)]
        # Here we add at the array's beginning, so we init head and tail at the array's end
        self.head = capacity - 1
        self.tail = capacity - 1
 
    def push(self, item):
        if item is None:
            raise ValueError("Cannot use None as a value in ring queue")
        # If we ran out of preallocated space, expand the array and move items
        if self.head == self.tail and self.items[self.head] is not None:
            new_array = [None for i in range(self.capacity * 2)]
            start_index = 0 if self.tail + 1 == self.capacity else self.tail + 1
            for i in range(start_index, start_index + self.capacity):
                new_array[i - start_index] = self.items[i - self.capacity]
            self.items = new_array
            # Move head to the end of moved data
            self.head = self.capacity - 1
            self.capacity *= 2
            # Move tail to the end of newly allocated space
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
  
class RingQueue2(RingQueue):
    def __init__(self, capacity: int = 8, growth_factor: float = 2.0):
        self.capacity = capacity
        self.growth_factor = growth_factor
        # None denotes an abscence of an item
        self.items = [None for i in range(capacity)]
        self.head = 0
        self.tail = capacity - 1

    def push(self, item):
        if item is None:
            raise ValueError("Cannot use None as a value in ring queue")
        # Precompute index of next item, since it will be used multiple times
        nextTail = (self.tail + 1) % self.capacity
        # If we ran out of preallocated space, expand the array and move items
        if self.head == nextTail and self.items[self.head] is not None:
            new_capacity = int(self.capacity * self.growth_factor)
            new_array = [None for i in range(new_capacity)]
            for i in range(self.head, self.head + self.capacity):
                new_array[i - self.head] = self.items[i - self.capacity]
            self.items = new_array
            self.tail = self.capacity - 1
            nextTail = self.capacity
            self.head = 0
            self.capacity = new_capacity
        self.items[nextTail] = item
        self.tail = nextTail
  
    def isEmpty(self) -> bool:
        return self.head == (self.tail + 1) % self.capacity and self.items[self.head] is None
 
    def pop(self):
        if self.isEmpty():
            raise IndexError("Ring queue is empty")
        value = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.capacity
        return value
  
    def peek(self):
        if self.isEmpty():
            raise IndexError("Ring queue is empty")
        return self.items[self.head]

if __name__ == "__main__":
    test_queues = [RingQueue1(4), RingQueue2(4, 1.5)]
    for queue in test_queues:
        queue.push(30)
        queue.push(100)
        queue.push(40)
        assert queue.peek() == 30
        assert queue.pop() == 30
        assert queue.peek() == 100
        queue.push(140)
        queue.push(70)
        queue.push(-70)
        queue.push(0)
        assert queue.pop() == 100
        [queue.pop() for _ in range(5)]
        assert queue.isEmpty()

