class ReverseArray:
    def __init__ (self):
        self.numbers = []
    
    def read_array(self, count):
        for i in range(count):
            self.numbers.append(int(input()))

    def reverse_array(self):
        l = 0
        r = len(self.numbers) - 1

        while l < r:
            self.numbers[l], self.numbers[r] = self.numbers[r], self.numbers[l]
            l += 1
            r -= 1
        return self.numbers

n = int(input())

reversearray = ReverseArray()
reversearray.read_array(n)
print(reversearray.reverse_array())
