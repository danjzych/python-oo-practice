class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        '''Create serial generator starting at self'''
        self.start = start
        self.next = start

    def __repr__(self):
        return f'instance of SerialGenerator starting at {self.start}'

    def generate(self):
        '''Increments self.next by one and return it'''
        currentValue = self.next
        self.next += 1
        return currentValue

    def reset(self):
        '''Resets self.next to initial start value'''
        self.next = self.start