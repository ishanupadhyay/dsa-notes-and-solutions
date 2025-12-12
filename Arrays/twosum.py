class TwoSum:
    def __init__ (self):
        self.numbers = []

    def read_array(self, count):
        for i in range(count):
            self.numbers.append(int(input()))
    
    def two_sum(self, target):

        hashmap = {}

        for num in range(len(self.numbers)):
            secondnumber = target - self.numbers[num]

            if secondnumber in hashmap:
                return [num, hashmap[secondnumber]]
            hashmap[self.numbers[num]] = num
        return []

n = int(input())

two_sum = TwoSum()
two_sum.read_array(n)
target = int(input())
print(two_sum.two_sum(target))
