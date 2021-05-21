import deal


@deal.inv(lambda buffer: buffer.max_size > 0)
class CircularBuffer:
    """
    Реализация структуры данных циклический буфер.
    """
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.__data = [None] * max_size
        self.head = 0
        self.tail = -1

    def is_empty(self):
        """Return True if the head of the CircularBuffer is equal to the tail,
        otherwise return False
        Runtime: O(1) Space: O(1)"""
        return self.tail == self.head

    def is_full(self):
        """Return True if the tail of the CircularBuffer is one before the head,
        otherwise return False
        Runtime: O(1) Space: O(1)"""
        return self.tail == (self.head - 1) % self.max_size

    def enqueue(self, item):
        """Insert an item at the back of the CircularBuffer
        Runtime: O(1) Space: O(1)"""
        if self.is_full():
            raise OverflowError(
                "CircularBuffer is full, unable to enqueue item")
        self.tail = (self.tail + 1) % self.max_size
        self.__data[self.tail] = item

    def front(self):
        """Return the item at the front of the CircularBuffer
        Runtime: O(1) Space: O(1)"""
        return self.__data[self.head]

    def dequeue(self):
        """Return the item at the front of the Circular Buffer and remove it
        Runtime: O(1) Space: O(1)"""
        if self.is_empty():
            raise IndexError("CircularBuffer is empty, unable to dequeue")
        item = self.__data[self.head]
        self.__data[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return item

    def __getitem__(self, item):
        return self.__data[item]


# Раскомментируйте следующую строку, чтобы получить ошибку контракта
# cb = CircularBuffer(-1)
