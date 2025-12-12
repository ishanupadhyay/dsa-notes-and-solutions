#rotate array k steps to the right
class RotateArray:
    def __init__ (self):
        self.numbers = []
    
    def read_array(self, count):
        for i in range(count):
            self.numbers.append(int(input()))

    def rotate_array_k_steps(self, k):
        numberoftimestorotate = k%len(self.numbers)
        partition = (len(self.numbers) - numberoftimestorotate) - 1

        l = 0
        r = partition
        self.reversearray(l,r)

        l = partition + 1
        r = len(self.numbers) - 1
        self.reversearray(l,r)

        l = 0
        r = len(self.numbers) - 1
        self.reversearray(l,r)

        return self.numbers


    def reversearray(self, l, r):
        while l < r:
            self.numbers[l],self.numbers[r] = self.numbers[r],self.numbers[l]
            l += 1
            r -= 1

n = int(input())
rotate_array = RotateArray()
rotate_array.read_array(n)
k = int(input())
print(rotate_array.rotate_array_k_steps(k))
