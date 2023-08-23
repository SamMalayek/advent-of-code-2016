from re import split


class Disc:
	def __init__(self, numPositions, curPosition):
		self.curTime = 0
		self.numPositions = numPositions
		self.curPosition = curPosition


def isPathClear(discs):
	for i, disc in enumerate(discs):
		if (disc.curPosition + i + 1) % disc.numPositions != 0:
			return False
	print(discs[0].curTime)
	return True


def main():
	raw = open('day15.txt', 'r').read().splitlines()
	discs = []
	for line in raw:
		parts = split(' |\.', line)
		numPositions, curPosition = int(parts[3]), int(parts[-2])
		discs.append(Disc(numPositions, curPosition))

	while not isPathClear(discs):
		for disc in discs:
			disc.curTime += 1
			disc.curPosition = (disc.curPosition + 1) % disc.numPositions


if __name__ == "__main__":
	main()
