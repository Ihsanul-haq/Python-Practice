class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be positive")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" *self.size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Number must be positive")
        if self.size + n > self.capacity:
            raise ValueError("Exceeds jar capacity")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Can not withdraw negative number")
        if self.size - n < 0:
            raise ValueError("Not enough cookies")
        self._size -= n
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
def main():
    jar = Jar()
    print("Empty jar: ", jar)
    jar.deposit(5)
    print("Deposit: ",jar)
    jar.withdraw(2)
    print("Withdraw: ",jar)
    print("Capacity is", jar.capacity)
    print("Size is", jar.size)
if __name__ == "__main__":

    main()
