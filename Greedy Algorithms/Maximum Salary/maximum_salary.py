# python3
from functools import cmp_to_key
from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def compare(x,y):
    return int(str(x)+str(y)) - int(str(y)+str(x))
def largest_number(numbers):
    numbers.sort(key = cmp_to_key(compare), reverse=True)
    sol = ""
    for i in numbers:
        sol = sol + str(i)
    return int(sol)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
