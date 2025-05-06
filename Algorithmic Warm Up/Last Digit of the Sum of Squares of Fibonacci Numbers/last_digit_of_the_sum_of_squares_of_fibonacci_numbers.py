# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_fibonacci(n):
    if n<=1:
        return n
    lis = [0,1]
    first = 0
    second = 1
    third = 0
    while True:
        third = first + second
        third = third%10
        lis.append(third)
        if lis[-1]==1 and lis[-2]==0:
            lis.pop()
            lis.pop()
            break
        first = second
        second = third
    return lis[n%len(lis)]

def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    if n==0:
        return 0
    temp = last_digit_of_fibonacci(n) * (last_digit_of_fibonacci(n) + last_digit_of_fibonacci(n-1))
    return temp%10

if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
