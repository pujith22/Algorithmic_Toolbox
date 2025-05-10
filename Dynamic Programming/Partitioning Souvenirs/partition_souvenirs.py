from collections import defaultdict
from itertools import product
from sys import stdin


def partition3_naive(values):
    for c in product(range(3), repeat=len(values)):
        sums = [[], [], []]
        for i in range(3):
            sums[i] = sum(values[k] for k in range(len(values)) if c[k] == i)
        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)
    values = list(values)
    # heuristic hack to pack larger values as soon as we can
    values.sort(reverse=True)
    total = sum(values)
    if total%3!=0:
        return 0
    target = total//3
    for mask in range(2**len(values)-1,-1,-1):
        tot = 0
        for j in range(len(values)):
            if (1<<j) & mask:
                tot = tot + values[j]
            if tot>=target:
                break
        if tot==target:
            lis = []
            for j in range(len(values)):
                if(1<<j) & mask == 0:
                    lis.append(values[j])
            dp = defaultdict()
            if helper(lis,target,len(lis)-1,dp):
                return 1
    return 0

def helper(lis,target,index,dp):
    if target==0:
        return True
    if index<0 or target<0:
        return False
    if dp.get((target,index),None) is not None:
        return dp[(target,index)]
    dp[(target,index)] = helper(lis,target,index-1,dp) or helper(lis,target-lis[index],index-1,dp)
    return dp[(target,index)]

if __name__ == '__main__':
    # stress test
    # for i in range(100):
    #     n = randint(1,12)
    #     lis = []
    #     for i in range(n):
    #         lis.append(randint(1,20))
    #     lis.append(3-sum(lis)%3)
    #     if partition3(lis) != partition3_naive(lis):
    #         print(lis)
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
