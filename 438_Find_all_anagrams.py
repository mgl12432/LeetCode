from collections import defaultdict
def anagram(val, anagram):

    p1, p2 = 0, 0
    n = len(anagram)
    totalLen = len(val)
    setBank = defaultdict(int)
    result = []

    for i in anagram:
        setBank[i] +=1

    while p2 < totalLen:

        if val[p2] in setBank and setBank[val[p2]] > 0 and n > p2-p1:
            setBank[val[p2]]-=1
            if n == p2-p1+1:
                result.append(p1)
            p2+=1

        elif ( val[p2] not in setBank or (val[p2] in setBank and setBank[val[p2]] == 0)) and p1 < p2:
            setBank[val[p1]]+=1
            p1+=1

        elif val[p2] not in setBank and p1 == p2:
            p1+=1
            p2+=1

    return result

result  = anagram("cbaebabacd", "abc") #[0, 6]

print(result)

# O(n+m) Time
# O(n) Space
