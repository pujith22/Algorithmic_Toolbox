# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared
def helper(points,start,end):
    if end-start+1<2:
        return 0
    if end-start+1==2:
        return distance_squared(points[start],points[end])
    if end-start+1==3:
        return min(min(distance_squared(points[start],points[start+1]),distance_squared(points[start+1],points[end])),distance_squared(points[start],points[end]))
    mid = start + (end-start)//2

    left_min = helper(points,start,mid)
    right_min = helper(points,mid+1,end)
    d = min(left_min,right_min)
    points_on_strip = []
    for i in range(start,end+1):
        point = points[i]
        if abs(point.x-points[mid].x)<=d:
            points_on_strip.append(point)
    # print(points_on_strip)
    points_on_strip.sort(key=lambda point: point.y)
    # print(points_on_strip)
    for i in range(len(points_on_strip)):
        for j in range(i+1,min(i+8,len(points_on_strip))):
            d = min(d,distance_squared(points_on_strip[i],points_on_strip[j]))
    return d


def minimum_distance_squared(points):
    points.sort(key=lambda point: point.x)
    return helper(points,0,len(points)-1)

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
