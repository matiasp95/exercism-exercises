class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def read(self):
        if len(self.buffer) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        r = self.buffer[0]
        self.buffer = self.buffer[1:]
        self.capacity += 1
        return r

    def write(self, data):
        if(self.capacity == 0):
            raise BufferFullException("Circular buffer is full")
        self.buffer.append(data)
        self.capacity -= 1

    def overwrite(self, data):
        if self.capacity != 0:
            self.write(data)
        else:
            self.buffer = self.buffer[1:]
            self.buffer.append(data)
    def clear(self):
        self.capacity = self.capacity + len(self.buffer)
        self.buffer = []

