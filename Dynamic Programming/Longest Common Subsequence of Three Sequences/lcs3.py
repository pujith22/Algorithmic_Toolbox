# python3
from collections import defaultdict


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    dp = defaultdict()
    return helper(first_sequence,second_sequence,third_sequence,len(first_sequence)-1,len(second_sequence)-1,len(third_sequence)-1,dp)

def helper(a,b,c,p,q,r,dp):
    if p==-1 or q==-1 or r==-1:
        return 0
    if dp.get((p,q,r),None) is not None:
        return dp[(p,q,r)]
    sol = 0
    if a[p]==b[q]==c[r]:
        sol = 1+helper(a,b,c,p-1,q-1,r-1,dp)
    sol = max(sol,helper(a,b,c,p-1,q-1,r,dp))
    sol = max(sol,helper(a,b,c,p-1,q,r-1,dp))
    sol = max(sol,helper(a,b,c,p-1,q,r,dp))
    sol = max(sol,helper(a,b,c,p,q-1,r-1,dp))
    sol = max(sol,helper(a,b,c,p,q-1,r,dp))
    sol = max(sol,helper(a,b,c,p,q,r-1,dp))
    dp[(p,q,r)] = sol
    return sol


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
