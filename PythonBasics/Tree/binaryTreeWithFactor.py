import collections
from collections import defaultdict


def numFactoredBinaryTrees(arr):
    arr.sort()
    l = defaultdict(int)
    for a in arr:
        temp = 1
        for b in arr:
            if b > a: break
            temp += (l[b] * l[a / b])
            print(l[a / b])
        print(temp)
        l[a] = temp
    return sum(l.values())


arr = [2, 4, 5]
print(numFactoredBinaryTrees(arr))
