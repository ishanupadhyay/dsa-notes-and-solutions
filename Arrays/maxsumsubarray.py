#kadane's algorithm
#find contiguous subarray with the largeset sum
#this is classic kadane's algorithm that returns maximum sub array sum and not the sub array.
#time complexity O(N)
#space complexity O(1)

class KadanesAlgorithm:
    def __init__ (self):
        self.nums = []
    
    def read_input(self, count):

        for _ in range(count):
            self.nums.append(int(input()))
    
    def maxsubarraysum(self):

        curr_sum = 0
        max_sum = float('-inf')

        for i in range(len(self.nums) - 1):

            curr_sum = curr_sum + self.nums[i]

            if curr_sum < 0:
                curr_sum = 0
            
            max_sum = max(curr_sum, max_sum)
        
        return max_sum

n = int(input())
maximumsubarraysum = KadanesAlgorithm()
maximumsubarraysum.read_input(n)
print(maximumsubarraysum.maxsubarraysum())
