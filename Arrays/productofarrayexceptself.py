#Return array where out[i] is product of all elements except arr[i], without division.
#Create prefix list meaning product of numbers before itself
#Create suffix list meaning product of numbers after itself
#Multiply to find the actual product
class ProductArray:
    def __init__ (self):
        self.numbers = []

    def read_array(self, count):
        for i in range(count):
            self.numbers.append(int(input()))
    
    def product_of_array(self):
        prefix = [1] * len(self.numbers)
        suffix = [1] * len(self.numbers)
        product_array = [0] * len(self.numbers)

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] * self.numbers[i-1]
        
        for i in range (1, len(suffix)):
            suffix[i] = suffix[i-1] * self.numbers[len(suffix) - i]
        
        for i in range(len(self.numbers)):
            product_array[i] = prefix[i] * suffix[len(self.numbers) - i - 1]

        return product_array

if __name__ == "__main__":
    n = int(input())
    productarray = ProductArray()
    productarray.read_array(n)
    print(productarray.product_of_array())
