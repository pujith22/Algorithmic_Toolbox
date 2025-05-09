# python3
from collections import defaultdict


def edit_distance(first_string, second_string):
    dp = defaultdict()
    return helper(first_string,second_string,len(first_string)-1,len(second_string)-1,dp)

def helper(a,b,l,m,dp):
    if l==-1 or m==-1:
        return max(l,m)+1
    if dp.get((l,m),None) is not None:
        return dp[(l,m)]
    insert = 1+helper(a,b,l,m-1,dp)
    delete = 1+helper(a,b,l-1,m,dp)
    replace = 1+helper(a,b,l-1,m-1,dp) if a[l]!=b[m] else helper(a,b,l-1,m-1,dp)
    dp[(l,m)] = min(min(insert,delete),replace)
    return dp[(l,m)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
