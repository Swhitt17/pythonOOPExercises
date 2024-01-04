"""Python serial number generator."""

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
    def __init__(self,start = 0):
        self.start = self.next = start

    def __repr__(self):
        """Show representation"""

    def generate(self):
        """Gets next sequential number"""
        self.next += 1
        return self.next - 1
        

    def reset(self):
        """Resets sequence back to start value"""
        self.next = self.start


