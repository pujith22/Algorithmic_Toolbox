def linear_search(keys,query):
    for i in range(len(keys)):
        if query==keys[i]:
            return i
    return -1
def binary_search(keys, query):
    # write your code here
    lo = -1
    hi = len(keys)
    while lo+1<hi:
        mid = lo + (hi-lo)//2
        ele = -float("Inf") if mid==-1 else float("Inf") if mid==len(keys) else keys[mid]
        if ele<query:
            lo = mid
        else:
            hi = mid
    if hi<len(keys) and keys[hi]==query:
        return hi
    return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
