def longestConsecutive(nums):

    maxCount = 0
    store = set(nums)

    for i in nums:
        count = 0
        curNum = i
        while curNum - 1 not in store and curNum in store:
            count += 1
            store.remove(curNum)
            curNum += 1
        maxCount = max(maxCount, count)
    return maxCount


input = [100,4,200,1,3,2]
output = longestConsecutive(input)
print(output)  # Output: 4

# O(n) Time complixity
# O(n) Space complixity
