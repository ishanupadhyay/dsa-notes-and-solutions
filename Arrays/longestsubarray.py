#return the length of the longest subarray whose sum is less than or equal to K
#Given array of non negative integer
class LongestSubarray:
    def __init__(self):
        self.number = []
    
    def read_array(self, count):
        for i in range(count):
            self.number.append(int(input()))
    
    def longestsubarray(self, k):
        left = 0
        curr_sum = 0
        right = 0
        length = 0

        for right in len(self.number):
            curr_sum = curr_sum + self.number[right]

            while curr_sum > k:
                curr_sum = curr_sum - self.number[left]
                left += 1
            
            length = max(length, right - left + 1)
        return length
