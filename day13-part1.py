import heapq
import math


# Uncomparable is to stop heapq.heappop from comparing elements beyond fScore in heap
class Uncomparable: 
	def __lt__(self, other):
		return False

	def __gt__(self, other):
		return False


def main():
	puzzleInput = int(open('day13.txt', 'r').read().rstrip())
	print(puzzleInput)
	goal = (31, 39)
	seen = set([(1, 1)])
	dirOffsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	
	def isWall(x, y):
		ones = format(x*x + 3*x + 2*x*y + y + y*y + puzzleInput, 'b').count('1')
		return ones % 2 == 1

	def getEuclDist(x1, x2, y1, y2):
		return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

	def getFScore(x, y, cost=0):
		return getEuclDist(x, goal[0], y, goal[1]) + cost

	startFScore = getFScore(1, 1)
	heap = [(startFScore, Uncomparable(), 1, 1, 0)]  # fScore, stopCompareObj, x, y, steps

	while heap:
		_, _, curX, curY, steps = heapq.heappop(heap)

		# Found goal
		if curX == goal[0] and curY == goal[1]:
			print(steps)
			quit()

		for xOffset, yOffset in dirOffsets:
			nextX, nextY = curX+xOffset, curY+yOffset
			if nextX < 0 or nextY < 0:
				continue
			if (nextX, nextY) in seen:
				continue
			if isWall(nextX, nextY):
				continue
			seen.add((nextX, nextY))

			heapq.heappush(heap, (getFScore(nextX, nextY, steps+1), Uncomparable(), nextX, nextY, steps+1))


if __name__ == "__main__":
	main()
