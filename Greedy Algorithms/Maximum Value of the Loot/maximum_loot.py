# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)
    value = 0
    while capacity>0 and len(weights)>0:
        max_value_per_weight = -float("Inf")
        max_index = -1
        for i in range(len(weights)):
            if max_value_per_weight < prices[i]/weights[i]:
                max_value_per_weight = prices[i]/weights[i]
                max_index = i
        value = value + min(capacity,weights[max_index])*max_value_per_weight
        capacity = capacity - min(capacity,weights[max_index])
        weights.pop(max_index)
        prices.pop(max_index)
    return value




if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
