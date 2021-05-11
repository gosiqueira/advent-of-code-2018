def get_input(day=1):
    inputs = []
    with open(f'inputs/input-{day:02d}.txt', 'r') as f:
        inputs = f.read().split()

    try:
        inputs = [int(elem) for elem in inputs]
    except:
        inputs = inputs

    return inputs

