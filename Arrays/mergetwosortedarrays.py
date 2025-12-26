class MergeSortedArray:
    def __init__ (self):
        self.nums1 = []
        self.nums2 = []
    
    def read_nums1(self, total_size, m):

        for _ in range(total_size):
            self.nums1.append(int(input()))
        
        self.m = m
    

    def read_nums2(self, n):

        for _ in range(n):
            self.nums2.append(int(input()))
        
        self.n = n
    
    def merge(self):

        i = self.m - 1
        j = self.n - 1

        k = self.m + self.n - 1

        while j >= 0:

            if i >= 0 and self.nums1[i] > self.nums2[j]:
                self.nums1[k] = self.nums1[i] 
                i -= 1
            
            else:
                self.nums1[k] = self.nums2[j]
                j -= 1
            k -= 1

        return self.nums1
