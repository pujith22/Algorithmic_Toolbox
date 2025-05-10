# python3
from collections import defaultdict

def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    dp_max = defaultdict()
    dp_min = defaultdict()
    return helper(dataset, 0,len(dataset)-1,dp_max,dp_min)

def helper(data,l,r,dp_max,dp_min,maxi=True):
    if l==r:
        return int(data[l])
    if maxi and dp_max.get((l, r),None) is not None:
        return dp_max[(l,r)]
    if not maxi and dp_min.get((l,r),None) is not None:
        return dp_min[(l,r)]
    max_sol = -float("Inf")
    min_sol = float("Inf")
    for k in range(l,r,2):
        left_max = helper(data,l,k,dp_max,dp_min)
        right_max = helper(data,k+2,r,dp_max,dp_min)
        left_min = helper(data,l,k,dp_max,dp_min,False)
        right_min = helper(data,k+2,r,dp_max,dp_min,False)
        if data[k+1]=='-':
            max_sol = max(max_sol,left_max - right_min)
            min_sol = min(min_sol,left_min - right_max)
        elif data[k+1]=='+':
            max_sol = max(max_sol,left_max+right_max)
            min_sol = min(min_sol,left_min + right_min)
        else:
            max_sol = max(max_sol,left_max * right_max)
            max_sol = max(max_sol, left_min * right_min)
            min_sol = min(min_sol,left_min * right_min)
    dp_max[(l,r)] = max_sol
    dp_min[(l,r)] = min_sol
    if not maxi:
        return min_sol
    return max_sol

if __name__ == "__main__":
    print(find_maximum_value(input()))
