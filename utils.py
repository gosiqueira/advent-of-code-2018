def get_input(day=1):
    inputs = []
    with open(f'inputs/input-{day:02d}.txt', 'r') as f:
        inputs = f.read().splitlines()

    try:
        inputs = [int(elem) for elem in inputs]
    except:
        inputs = inputs

    return inputs


def manhatan_dist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
