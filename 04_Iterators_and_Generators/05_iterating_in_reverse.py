class Countdown:
    def __init__(self, start):
        self._start = start

    def __iter__(self):
        n = self._start
        while n > 0:
            yield n
            n -= 1


class CountdownWithR(Countdown):
    def __reversed__(self):
        n = 1
        while n <= self._start:
            yield n
            n += 1


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)
    print()

    for cnt in Countdown(3):
        print(cnt)
    print()

    # reversed() only works if the object in question has a size that can
    # be determined or the object implements a __reversed__() special method.
    for cnt in reversed(list(Countdown(3))):
        print(cnt)
    print()
    for cnt in reversed(CountdownWithR(3)):
        print(cnt)
