def zippo(xs, ys):
    def loop(xs, ys, zs):
        if xs == [] or ys == []:
            return zs + xs + ys
        else:
            return loop(xs[1:], ys[1:], zs + [xs[0] + ys[0]])
    return loop(xs, ys, [])

def zippo(xs, ys):
    zs = []
    while not (xs == [] or ys == []):
        zs = zs + [xs[0] + ys[0]]
        xs = xs[1:]
        ys = ys[1:]
    return zs + xs + ys

print(zippo([], []))  # []
print(zippo([2, 7, 4], [7, 2, 5]))  # [9,9,9]
print(zippo([2, 7, 4], [7, 2, 5, 9, 9]))  # [9,9,9,9,9]
print(zippo([2, 7, 4, 9, 9], [7, 2, 5]))  # [9,9,9,9,9]