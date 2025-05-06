# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10

def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    lis = [0,1]
    first = 0
    second = 1
    third = 0
    while True:
        third = first + second
        third = third %10
        lis.append(third)
        if lis[-1]==1 and lis[-2]==0:
            lis.pop()
            lis.pop()
            break
        first = second
        second = third
    tot = sum(lis)*((n+1)//len(lis))
    for i in range((n+1)%len(lis)):
        tot = tot + lis[i]
    return tot%10
def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    temp = last_digit_of_the_sum_of_fibonacci_numbers(to_index) - (last_digit_of_the_sum_of_fibonacci_numbers(from_index-1) if from_index>0 else 0 )
    temp = (temp + 10)%10
    return temp


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
