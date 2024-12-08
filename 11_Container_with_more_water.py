class Solution:
    def maxArea(self, val: List[int]) -> int:
        p1, p2 = 0, len(val)-1
        maximumCapacity = 0

        while p1 < p2:
            smallWall = min(val[p1], val[p2])
            maximumCapacity = max(maximumCapacity, (p2-p1) * smallWall)

            if val[p1] < val[p2]:
                p1+=1
            else:
                p2-=1

        return maximumCapacity


# O(n) Time
# O(1) space
