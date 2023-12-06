import math

test_input = [
    {"time": 7, "distance": 9},
    {"time": 15, "distance": 40},
    {"time": 30, "distance": 200},
]

input = [
    {"time": 47, "distance": 207},
    {"time": 84, "distance": 1394},
    {"time": 74, "distance": 1209},
    {"time": 67, "distance": 1014},
]


def find_zero_points_quadratic(a, b, c):
    return [
        (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a),
        (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a),
    ]


def get_distance(max_time, charge_time):
    return (max_time - charge_time) * charge_time


def get_charge_time_for_max_distance(max_time):
    return int(max_time / 2)


result1 = 1

for race in input:
    max_time = race["time"]
    distance_record = race["distance"]
    zpts = find_zero_points_quadratic(1, -max_time, distance_record)
    zpts.sort()
    print("charge times for record distance:", zpts[0], "and", zpts[1])
    charge_time_max_distance = get_charge_time_for_max_distance(max_time)
    max_distance = get_distance(max_time, charge_time_max_distance)
    print(f"charge time {charge_time_max_distance} gives max distance {max_distance}")
    lower_bound = math.floor(zpts[0] + 1)
    upper_bound = math.ceil(zpts[1] - 1)
    print(
        f"all ints in range [{lower_bound}, {upper_bound}] are ways to beat the record"
    )
    n = upper_bound - lower_bound + 1
    print("number of ways is", n)
    result1 *= n

    print()

print("part 1: ", result1)
print()

# part 2
test_input_race = {"time": 71530, "distance": 940200}
input_race = {"time": 47847467, "distance": 207139412091014}


def do(race):
    max_time = race["time"]
    distance_record = race["distance"]
    zpts = find_zero_points_quadratic(1, -max_time, distance_record)
    zpts.sort()
    lower_bound = math.floor(zpts[0] + 1)
    upper_bound = math.ceil(zpts[1] - 1)
    n = upper_bound - lower_bound + 1
    return n


print("part 2: ", do(input_race))
