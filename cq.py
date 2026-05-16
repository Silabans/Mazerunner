class CircularQueue:
    """Circular Queue implemented as Array.

    Methods
        - enqueue(item)
          Adds item at the end of the queue.

        - dequeue()
          Returns the first item in the queue.
    """

    def __init__(self, size: int):
        self.size = size
        self._data = [None] * size
        self.head = -1
        self.tail = 0
        

    def __repr__(self) -> str:
        return f"CircularQueue({self.size})"

    def enqueue(self, item: tuple[int, int]) -> None:
        """Add item at the end of the queue.

        Arguments
            - item
              The item to be added.

        Return
            None
        """
        if self.tail == -1:
            raise IndexError("queue is full")
        if self.head == -1:
            self.head = self.tail
        
        self._data[self.tail] = item
        next_tail = (self.tail + 1) % self.size
        if next_tail == self.head:
            self.tail = -1
        else:
            self.tail = next_tail

    def push(self, item):
        """ Ensures a unified interface between Queue and Stack for ease in the maze loop. """
        self.enqueue(item)


    def dequeue(self) -> tuple[int, int]:
        """Return the item at the head of the queue.

        Arguments
            None

        Return
            item
        """
        if self.head == -1:
            raise IndexError('queue is empty; nothing to dequeue')
        
        #if queue is full, the tail wraps back to the current index of the head
        if self.tail == -1:
            self.tail = self.head
        
        value = self._data[self.head]
        
        # if the head exceed the tail, then the list would be empty, but the cq must
        # still allow head to have a greater index than the tail (wrap around)
        next_head = (self.head + 1) % self.size
        if next_head == self.tail:
            self.head = -1
        else:
            self.head = next_head

        return value
    
    def pop(self):
        """ Ensures a unified interface between Queue and Stack for ease in the maze loop """
        self.dequeue()
    
    def contains(self, item: tuple[int, int]):
        for i in range(self.size):
            if item == self._data[(self.head + i) % self.size]:
                return True
        return False

if __name__ == "__main__":
    cq = CircularQueue(5)
    for i in range(5):
        cq.enqueue((i, i))
    print(cq._data)
    print(cq.contains((1, 2)))