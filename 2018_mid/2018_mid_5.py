def zippo(xs, ys):
    if xs == [] or ys == []:
        return xs + ys
    else:
        return [xs[0] + ys[0]] + zippo(xs[1:], ys[1:])


def zippo(xs, ys):
    def loop(xs, ys, zs):
        if xs == [] or ys == []:
            return zs + xs + ys
        else:
            return loop(xs[1:], ys[1:], zs + [xs[0] + ys[0]])

    return loop(xs, ys, [])

print(zippo([], []))  # []
print(zippo([2, 7, 4], [7, 2, 5]))  # [9,9,9]
print(zippo([2, 7, 4], [7, 2, 5, 9, 9]))  # [9,9,9,9,9]
print(zippo([2, 7, 4, 9, 9], [7, 2, 5]))  # [9,9,9,9,9]