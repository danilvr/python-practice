import random
from circular_buffer import CircularBuffer


def test_circular_buffer():
    tests = 1000
    buffer_size = 100
    data = [None] * buffer_size
    buffer = CircularBuffer(buffer_size)
    head = 0
    tail = -1

    for i in range(tests):
        if tail != (head - 1) % buffer_size:
            x = random.getrandbits(8)
            buffer.enqueue(x)
            tail = (tail + 1) % buffer_size
            data[tail] = x
            assert data[head] == buffer.front()
        else:
            dequeue_count = random.randint(1, abs(tail - head))
            for _ in range(dequeue_count):
                buffer.dequeue()
                data[head] = None
                head = (head + 1) % buffer_size

        for j in range(buffer_size):
            assert buffer[j] == data[j]

    try:
        for i in range(buffer_size):
            buffer.enqueue(i)
    except OverflowError:
        pass

    try:
        for _ in range(buffer_size):
            buffer.dequeue()
    except IndexError:
        pass
