def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


if __name__ == '__main__':
    for n in frange(0, 4, 0.5):
        print(n)

    print(list(frange(0, 1, 0.125)))
