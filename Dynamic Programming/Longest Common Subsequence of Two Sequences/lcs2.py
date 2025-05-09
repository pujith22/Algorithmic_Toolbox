# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    dp = dict()
    return helper(first_sequence,second_sequence,len(first_sequence)-1,len(second_sequence)-1,dp)
def helper(a,b,l,m,dp):
    if l==-1 or m==-1:
        return 0
    if dp.get((l,m),None) is not None:
        return dp[(l,m)]
    sol = 0
    if a[l]==b[m]:
        sol = 1+helper(a,b,l-1,m-1,dp)
    else:
        sol = max(helper(a,b,l-1,m,dp),helper(a,b,l,m-1,dp))
    dp[(l,m)] = sol
    return sol



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
