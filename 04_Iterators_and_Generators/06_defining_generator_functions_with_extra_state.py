import os
from collections import deque


class LineHistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line.strip()))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == '__main__':
    RELATIVE_PATH = 'inputs/test.txt'

    file_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(file_dir, RELATIVE_PATH)

    with open(file_path) as f:
        lines = LineHistory(f)
        for line in lines:
            if 'python' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline))
