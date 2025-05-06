# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    if n<=1:
        return n
    lis = [0, 1]
    first = 0
    second = 1
    third = 0
    while True:
        third = first+second
        third = third%m
        lis.append(third)
        if lis[-1]==1 and lis[-2]==0:
            lis.pop()
            lis.pop()
            break
        first = second
        second = third
    n = n%len(lis)
    return lis[n]

if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
