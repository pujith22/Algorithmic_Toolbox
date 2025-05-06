# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    tot = 0
    for i in range(1,10**9):
        tot = tot+i
        if tot>n:
            break
        summands.append(i)

    summands[-1] = summands[-1]+(n-sum(summands))
    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
