nums = [100,4,200,1,3,2]

hash_set = set()
length = 1
max_length = 0

for i in nums:
    hash_set.add(i)


for i in hash_set:
    if i - 1 not in hash_set:
        curr = i
        length = 1
    while curr + 1 in hash_set:
        curr += 1
        length += 1
    max_length = max(length, max_length)

print(max_length)
