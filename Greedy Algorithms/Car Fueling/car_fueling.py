# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    fuel = m
    count = 0
    for i in range(len(stops)):
        fuelNeededToReach = stops[i] - (stops[i-1] if i>0 else 0)
        if fuel<fuelNeededToReach:
            return -1
        fuel = fuel - fuelNeededToReach
        if (stops[i+1] if i<len(stops)-1 else d)-stops[i]>fuel:
            fuel = m
            count = count +1
    if d-stops[-1] > fuel:
        return -1
    return count




if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
