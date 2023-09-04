from re import split


class Disc:
    def __init__(self, numPositions, curPosition):
        self.curTime = 0
        self.numPositions = numPositions
        self.curPosition = curPosition


def main():
    raw = open('day15.txt', 'r').read().splitlines()
    discs = []
    for line in raw:
        parts = split(' |\.', line)
        numPositions, curPosition = int(parts[3]), int(parts[-2])
        discs.append(Disc(numPositions, curPosition))

    isPathClear = False
    while not isPathClear:
        isPathClear = True
        for i, disc in enumerate(discs):
            disc.curTime += 1
            disc.curPosition = (disc.curPosition + 1) % disc.numPositions
            if (disc.curPosition + i + 1) % disc.numPositions != 0:
                isPathClear = False
    print(discs[0].curTime)


if __name__ == "__main__":
    main()
