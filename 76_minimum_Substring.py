def min_window(val, anagram):
    p1, p2 = 0, 0
    setBank = {}
    unUsedCount = len(anagram)

    for i in anagram:
        setBank[i] = setBank.get(i, 0) + 1

    filter = [(i, char) for i, char in enumerate(val) if char in setBank]

    min_length = float("inf")
    min_window_start = 0

    while p2 < len(filter):
        char = filter[p2][1]

        if setBank[char] > 0:
            unUsedCount -= 1

        setBank[char] -= 1
        p2 += 1

        while unUsedCount == 0:
            start = filter[p1][0]
            end = filter[p2-1][0]

            if end - start + 1 < min_length:
                min_length = end - start + 1
                min_window_start = start

            char = filter[p1][1]
            setBank[char] += 1
            if setBank[char] > 0:
                unUsedCount += 1
            p1 += 1

    return val[min_window_start:min_window_start + min_length] if min_length != float("inf") else ""

result = min_window("ADOBECODEBANC", "ABC")
print(result)  # Expected output: "BANC"

# Time : O(n+m)
# Space : O(n+m)
