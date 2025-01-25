def subarraySum(nums, k):

    bankStore = {0:1}
    count = 0
    total = 0

    for i in nums:
        total += i
        if total-k in bankStore:
            count+=bankStore[total-k]

        bankStore[total] = bankStore.get(total, 0) + 1
    return count



input = [1,1,1]
k = 2
output = subarraySum(input, k)
print(output)  # Output: 2

# O(n) Time complixity
# O(n) Space complixity
