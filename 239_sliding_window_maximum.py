from collections import deque

def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []

    result = []
    dq = deque()
    p1, p2 = 0, 0

    while p2 < len(nums):
        while dq and nums[dq[-1]] < nums[p2]:
            dq.pop()

        dq.append(p2)

        if dq[0] < p1:
            dq.popleft()

        if (p2 + 1) >= k:
            result.append(nums[dq[0]])
            p1 += 1

        p2 += 1

    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
output = max_sliding_window(nums, k)
print(output)  # Output: [3, 3, 5, 5, 6, 7]

# O(n) Time complixity
# O(n+k) Space complixity
