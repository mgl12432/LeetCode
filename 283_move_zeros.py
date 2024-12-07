class Solution:
    def moveZeroes(self, val: List[int]) -> None:
        p1, p2 = 0,0
        valLen = len(val)

        while p1 < valLen and p2 < valLen:
            if val[p1] != 0:
                p1+=1
                p2+=1

            elif val[p2] == 0:
                p2+=1

            else:
                val[p1], val[p2] = val[p2], val[p1]
