from functools import cache

# process input
f = open("Day19\data.txt")
# f = open("Day19\data1.txt")
input1 = f.readlines()
towel_arr = input1[0].rstrip().split(sep=", ")

designs = []
for i in range(2, len(input1)):
    designs.append(input1[i].rstrip())

# build trie from towels
t_trie = {}
for t in towel_arr:
    t_ptr = t_trie
    for c in t:
        t_ptr[c] = t_ptr.setdefault(c, {})
        t_ptr = t_ptr[c]
    t_ptr["end"] = 0

# dfs a string based on if a slice of letters exists in a trie with a "end" point
@cache
def isPossiblePattern(des):
    # true if all matches have been found up to the end of the string
    if len(des) == 0:
        return 1
    
    res = 0
    # set a ptr to trie to dive into a trie pattern from the current i
    t_ptr = t_trie
    # loop for a pattern up to len(des)
    for i in range(len(des)):
        # if a letter matches from i
        if des[i] in t_ptr:
            # update t ptr to the trie of current matched letter
            t_ptr = t_ptr[des[i]]

            # check if the current trie location represents a pattern by containing end
            if "end" in t_ptr:
                # check for next pattern
                res += isPossiblePattern(des[i+1:])
        else:
            return res   
    return res

res = 0
for des in designs:
    res += isPossiblePattern(des)
print(res)