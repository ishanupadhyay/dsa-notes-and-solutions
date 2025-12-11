#remove duplicates in place and return the length of the array
class RemoveDuplicates:
    def __init__ (self):
        self.numbers = []
    
    def read_array(self, count):
        for i in range(count):
            self.numbers.append(int(input()))
    
    def remove_duplicates_inplace(self):
        slow = 0

        for fast in range(1, len(self.numbers)):

            if self.numbers[slow] != self.numbers[fast]:
                slow += 1
                self.numbers[slow] = self.numbers[fast]
        return slow + 1

n = int(input())
removeduplicates = RemoveDuplicates()
removeduplicates.read_array(n)
print('Length after removing duplicates: ', removeduplicates.remove_duplicates_inplace())
