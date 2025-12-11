class CreateArray:
    def __init__(self):
        self.numbers = []
    
    def read_numbers(self, count):
        for i in range(count):
            self.numbers.append(int(input()))
    
    def find_maximum(self):

        maximum = float('-inf')
        for num in self.numbers:
            if maximum < num:
                maximum = num
        return maximum

n = int(input())
createarray = CreateArray()
createarray.read_numbers(n)

print('Maximum number: ', createarray.find_maximum())
