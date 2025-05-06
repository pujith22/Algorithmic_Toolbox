# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments.sort(key = lambda x: x[1])
    lis = []
    i = 0
    while i<len(segments):
        point = segments[i][1]
        lis.append(point)
        while i<len(segments) and segments[i][0] <= point <= segments[i][1]:
            i = i+1
    return lis




if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
