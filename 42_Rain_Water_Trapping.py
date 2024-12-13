
def trapWater(val):

    leftMax, rightMax = 0,0
    p1, p2 = 0, len(val)-1

    count = 0

    while p1 < p2:

        leftMax = max(leftMax, val[p1])
        rightMax = max(rightMax, val[p2])

        p1Vacant = leftMax - val[p1]
        p2Vacant = rightMax - val[p2]

        if p1Vacant != 0:
            count+=p1Vacant
        if p2Vacant != 0:
            count += p2Vacant

        if val[p1] < val[p2]:
            p1 += 1
        else:
            p2 -=1


    return count

result  = trapWater([4,2,0,3,2,5]) # 9

print(result)

# O(n) Time
# O(n) Space
