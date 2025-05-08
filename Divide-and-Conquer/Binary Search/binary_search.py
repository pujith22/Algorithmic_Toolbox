# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    l = 0
    r = len(keys)-1
    while l<=r:
        mid = l+(r-l)//2
        if keys[mid]==query:
            return mid
        elif keys[mid]<query:
            l = mid+1
        else:
            r = mid-1
    return -1


if __name__ == '__main__':
    n = input()
    input_keys = list(map(int, input().split()))
    m = input()
    input_queries = list(map(int, input().split()))

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
