class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.current_quantity = 0


    def __str__(self):
        return "🍪" * self.current_quantity


    def deposit(self, n):
        if self.current_quantity + n <= self.capacity:
            self.current_quantity += n
        else:
            raise ValueError


    def withdraw(self, n):
        if self.current_quantity - n >= 0:
            self.current_quantity -= n
        else:
            raise ValueError


    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, capacity):
        if isinstance(capacity, int) and capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError


    @property
    def size(self):
        return self.current_quantity