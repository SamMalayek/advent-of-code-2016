from collections import deque
from itertools import permutations


def main():
    raw = open('day24.txt', 'r').read().splitlines()
    grid = [list(l) for l in raw]

    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # NxN matrix of distMatrix between each node
    distMatrix = [[99999 for _ in range(8)] for _ in range(8)]
    targets = {}
    targetsRev = {}

    # Collect all targets
    seen = set()
    q = deque([(1, 1)])
    while q:
        row, col = q.popleft()

        if grid[row][col].isnumeric():
            targets[int(grid[row][col])] = (row, col)
            targetsRev[(row, col)] = int(grid[row][col])

        for rowOffset, colOffset in dirs:
            nextRow = rowOffset+row
            nextCol = colOffset+col

            if grid[nextRow][nextCol] != '#' and (nextRow, nextCol) not in seen:
                seen.add((nextRow, nextCol))
                q.append((nextRow, nextCol))

    # Populate the distMatrix
    for targetRow, targetCol in targets.values():
        seen = set()
        q = deque([(0, targetRow, targetCol)])  # dist, targetRow, targetCol
        while q:
            dist, row, col = q.popleft()

            if (row, col) in targetsRev:
                fromm = targetsRev[(targetRow, targetCol)]
                to = targetsRev[(row, col)]
                distMatrix[fromm][to] = min(dist, distMatrix[fromm][to])
                distMatrix[to][fromm] = min(dist, distMatrix[to][fromm])

            for rowOffset, colOffset in dirs:
                nextRow = rowOffset+row
                nextCol = colOffset+col

                if grid[nextRow][nextCol] != '#' and (nextRow, nextCol) not in seen:
                    seen.add((nextRow, nextCol))
                    q.append((dist+1, nextRow, nextCol))

    # Could use Bellman-Held-Karp
    # Currently using O(N!) brute force. Perfectly fine for this input size.
    minDist = 9999999999
    for perm in permutations(range(0, 8)):
        cost = 0
        permList = list(perm)
        for i in range(1, len(permList)):
            cost += distMatrix[permList[i-1]][permList[i]]
        cost += distMatrix[permList[0]][permList[-1]]
        minDist = min(minDist, cost)

    print(minDist)


if __name__ == "__main__":
    main()
