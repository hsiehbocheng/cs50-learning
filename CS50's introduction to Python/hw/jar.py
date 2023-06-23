def main():
    x = Jar()
    print(x)
    x.deposit(5)
    print(x.size)
    print(str(x))

# https://cs50.harvard.edu/python/2022/psets/8/jar/
class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
    
    def __str__(self):
        return  "🍪"*self.size
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Invalid size")
        self._size = size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Exceed capacity")
        self.size += n
    
    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies")
        self.size -= n
        
    
if __name__ == "__main__":
    main()