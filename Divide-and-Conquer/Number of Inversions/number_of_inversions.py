# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if  a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def merge(arr,left,mid,right):
    count = 0
    temp = []
    ptr1 = left
    ptr2 = mid+1
    while ptr1<=mid and ptr2<=right:
        if arr[ptr1]<=arr[ptr2]:
            temp.append(arr[ptr1])
            ptr1 = ptr1+1
        else:
            temp.append(arr[ptr2])
            count = count + (mid-ptr1+1)
            ptr2 = ptr2+1
    while ptr1<=mid:
        temp.append(arr[ptr1])
        ptr1 = ptr1+1
    while ptr2<=right:
        temp.append(arr[ptr2])
        ptr2 = ptr2+1
    for i in temp:
        arr[left]=i
        left = left+1
    return count
def compute_inversions_helper(array,left,right):
    if left>=right:
        return 0
    mid = left + (right-left)//2

    inversion_count_left_half = compute_inversions_helper(array,left,mid)
    inversion_count_right_half = compute_inversions_helper(array,mid+1,right)

    inversion_count = merge(array,left,mid,right)

    return inversion_count+inversion_count_left_half+inversion_count_right_half
def compute_inversions(array):
    return compute_inversions_helper(array[:],0,len(array)-1)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
