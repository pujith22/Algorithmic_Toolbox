# python3

from random import randint


def partition3(array, left, right):
    ptr = left
    traverser = left+1
    while traverser<=right:
        if array[traverser]<array[left]:
            ptr = ptr+1
            array[ptr], array[traverser] = array[traverser], array[ptr]
        traverser = traverser+1
    array[ptr], array[left] = array[left], array[ptr]
    traverser = ptr+1
    ptr2 = ptr
    while traverser<=right:
        if array[traverser]==array[ptr]:
            ptr2 = ptr2+1
            array[ptr2], array[traverser] = array[traverser], array[ptr2]
        traverser = traverser+1
    return ptr,ptr2

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    ptr1, ptr2 = partition3(array,left,right)
    randomized_quick_sort(array, left, ptr1-1)
    randomized_quick_sort(array,ptr2+1,right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
