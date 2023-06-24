import re
import heapq

class Uncomparable: # Uncomparable is to stop heapq.heappop from comparing elements beyond fScore in heap
    def __lt__(self, other):
        return False
    def __gt__(self, other):
        return False

def main():
	lines = open('day11.txt', 'r').read().splitlines()
	floors = [[] for _ in range(4)]  # floor 1 = index 0, floor 4 = index 3
	totalItems = 0
	movedDown = {}  # Heuristic to prevent moving items down floors too much unnecessarily
	resp = 9999999999
	memo = {}

	def calcFScore(curFloors, steps=0):  # A* heuristic
		return len(curFloors[2]) + len(curFloors[1]) * 1.5 + len(curFloors[0]) * 2 + steps

	def hashCurFloors(curFloors):
		return tuple(tuple(sorted(floor)) for floor in curFloors)

	def floorFails(curFloor):  # Validates that the floor adheres to the radiation rules
		curFloorMs = set([c[0] for c in curFloor if c[1] == 'm'])
		curFloorGs = set([c[0] for c in curFloor if c[1] == 'g'])
		noPairMs = curFloorMs - curFloorGs

		if noPairMs and curFloorGs:
			return True
		return False

	for i, line in enumerate(lines[:3]):
		parts = list(filter(None, re.split(' a | and', line)))[1:]
		for part in parts:
			firstWord, secondWord = part.split(' ')
			floors[i].append(firstWord[0]+secondWord[0])
			totalItems += 1
			movedDown[firstWord[0]+secondWord[0]] = 0

	startFScore = calcFScore(floors)
	argsHeap = [(startFScore, Uncomparable(), floors, 0, 0, movedDown)]

	while argsHeap:
		fScore, _, curFloors, elevatorFloor, steps, curMovedDown = heapq.heappop(argsHeap)
		# Avoid traversing recursion tree where already seen
		curHash = (hashCurFloors(curFloors), elevatorFloor)
		if curHash in memo:
			continue
		memo[curHash] = True
		# Base case
		if len(curFloors[-1]) == totalItems:
			resp = min(resp, steps)
			continue

		if elevatorFloor < 3:  # Can move up
			# Move up with 1 item
			for item in curFloors[elevatorFloor]:
				newCurFloors = [floor[:] for floor in curFloors]
				newCurFloors[elevatorFloor] = [i for i in newCurFloors[elevatorFloor] if i != item]
				newCurFloors[elevatorFloor+1] = list(newCurFloors[elevatorFloor+1]) + [item]

				if floorFails(newCurFloors[elevatorFloor]) or floorFails(newCurFloors[elevatorFloor+1]):
					continue
				curMovedDown[item] = 0

				curFScore = calcFScore(newCurFloors, steps+1)
				heapq.heappush(argsHeap, (curFScore, Uncomparable(), newCurFloors, elevatorFloor+1, steps + 1, dict(curMovedDown)))
			# Move up with 2 items
			for item1 in curFloors[elevatorFloor]:
				for item2 in curFloors[elevatorFloor]:
					if item1 == item2:
						continue
					newCurFloors = [floor[:] for floor in curFloors]
					newCurFloors[elevatorFloor] = [i for i in newCurFloors[elevatorFloor] if i not in {item1, item2}]
					newCurFloors[elevatorFloor+1] = list(newCurFloors[elevatorFloor+1]) + [item1, item2]

					if floorFails(newCurFloors[elevatorFloor]) or floorFails(newCurFloors[elevatorFloor+1]):
						continue
					curMovedDown[item1] = 0
					curMovedDown[item2] = 0
	
					curFScore = calcFScore(newCurFloors, steps+1)
					heapq.heappush(argsHeap, (curFScore, Uncomparable(), newCurFloors, elevatorFloor+1, steps + 1, dict(curMovedDown)))

		if elevatorFloor != 0:  # Can move down
			# Move down with 1 item
			for item in curFloors[elevatorFloor]:
				if curMovedDown[item] > 0:
					continue
				newCurFloors = [floor[:] for floor in curFloors]
				newCurFloors[elevatorFloor] = [i for i in newCurFloors[elevatorFloor] if i != item]
				newCurFloors[elevatorFloor-1] = list(newCurFloors[elevatorFloor-1]) + [item]

				if floorFails(newCurFloors[elevatorFloor]) or floorFails(newCurFloors[elevatorFloor-1]):
					continue
				curMovedDown[item] += 1

				curFScore = calcFScore(newCurFloors, steps+1)
				heapq.heappush(argsHeap, (curFScore, Uncomparable(), newCurFloors, elevatorFloor-1, steps + 1, dict(curMovedDown)))
			# Move down with 2 items
			for item1 in curFloors[elevatorFloor]:
				for item2 in curFloors[elevatorFloor]:
					if item1 == item2:
						continue
					if curMovedDown[item1] > 0 or curMovedDown[item2] > 0:
						continue
					newCurFloors = [floor[:] for floor in curFloors]
					newCurFloors[elevatorFloor] = [i for i in newCurFloors[elevatorFloor] if i not in {item1, item2}]
					newCurFloors[elevatorFloor-1] = list(newCurFloors[elevatorFloor-1]) + [item1, item2]

					if floorFails(newCurFloors[elevatorFloor]) or floorFails(newCurFloors[elevatorFloor-1]):
						continue
					curMovedDown[item1] += 1
					curMovedDown[item2] += 1
	
					curFScore = calcFScore(newCurFloors, steps+1)
					heapq.heappush(argsHeap, (curFScore, Uncomparable(), newCurFloors, elevatorFloor-1, steps + 1, dict(curMovedDown)))

	print(resp)

if __name__ == "__main__":
	main()
