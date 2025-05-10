# python3
from collections import defaultdict
from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    dp = defaultdict()
    return helper(capacity,weights,len(weights)-1,dp)

def helper(capacity,weights,index,dp):
    if capacity<=0 or index<0:
        return 0
    if dp.get((capacity,index),None) is not None:
        return dp[(capacity,index)]
    sol = 0
    if capacity>=weights[index]:
        sol = max(weights[index]+helper(capacity-weights[index],weights,index-1,dp),helper(capacity,weights,index-1,dp))
    else:
        sol = helper(capacity,weights,index-1,dp)
    dp[(capacity,index)] = sol
    return sol



if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
