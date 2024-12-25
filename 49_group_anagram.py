
def groupAnagrams(strs):

    mapper={}

    for s in strs:

        key = ''.join(sorted(s))

        if key not in mapper:

            mapper[key]=[]

        mapper[key].append(s)

    return [mapper[val] for val in mapper]



strs = ["eat","tea","tan","ate","nat","bat"]
output = groupAnagrams(strs)
print(output)  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# O(m n logn) Time complixity
# O(m n) Space complixity
