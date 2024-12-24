def twoSum(nums, target):

    setBank = {}

    for idx in range(len(nums)):

        remains = target - nums[idx]

        if remains in setBank:
            return [setBank[remains], idx]
        else:
            setBank[nums[idx]] = idx

    return []


nums = [2,7,11,15]
target = 9
output = twoSum(nums, target)
print(output)  # Output: [0,1]

# O(n) Time complixity
# O(n) Space complixity
