# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    maxi = -float("Inf")
    maxPos = -1
    for i in range(len(numbers)):
        if(numbers[i]>maxi):
            maxi = numbers[i]
            maxPos = i
    secondMaxi = -float("Inf")
    for i in range(len(numbers)):
        if i!=maxPos and numbers[i]>secondMaxi:
            secondMaxi = numbers[i]
    return maxi * secondMaxi


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
