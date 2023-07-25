import heapq


def main():
	puzzleInput = int(open('day13.txt', 'r').read().rstrip())
	seen = set([(1, 1)])
	dirOffsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	
	def isWall(x, y):
		ones = format(x*x + 3*x + 2*x*y + y + y*y + puzzleInput, 'b').count('1')
		return ones % 2 == 1

	heap = [(0, 1, 1)]  # steps, x, y

	while heap:
		steps, curX, curY = heapq.heappop(heap)

		for xOffset, yOffset in dirOffsets:
			nextX, nextY = curX+xOffset, curY+yOffset
			if nextX < 0 or nextY < 0:
				continue
			if (nextX, nextY) in seen:
				continue
			if isWall(nextX, nextY):
				continue
			if steps+1 == 51:
				continue
			seen.add((nextX, nextY))
			heapq.heappush(heap, (steps+1, nextX, nextY))

	print(len(seen))


if __name__ == "__main__":
	main()
