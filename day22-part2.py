from collections import deque


class Node:
    def __init__(self, path, size=0, used=0, avail=0):
        self.path = path
        self.size = size
        self.used = used  # in Terabytes
        self.avail = avail


# We'll move data from the Source node (node in front of Goal node) to Sink node.
# Each "move", we'll identify a Source and Sink node, unless we can move the
# Goal node forward.
# Note: I prefer to break code into functions only if it reduces repetition, otherwise I prefer
# to use comments to break up code.
def main():
    raw = open('day22.txt', 'r').read().splitlines()
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    maxX = 0
    maxY = 0
    nodes = {}
    immovableNodes = set()

    # We'll maintain a sorted list of nodes (sorted by available capacity) to identify
    # the Sink node. This assumes there's only one Sink node in the grid.
    nodesSortedAvailCapacity = []

    for line in raw[2:]:
        path, size, used, avail, _ = line.split()

        _, x, y = path.split('-')
        x = int(x[1:])
        y = int(y[1:])
        maxX = max(maxX, x)
        maxY = max(maxY, y)
        # [:-1] to remove the 'T' from the number of terabytes.
        nodes[(x, y)] = Node((x, y), int(size[:-1]), int(used[:-1]), int(avail[:-1]))
        if int(used[:-1]) > 100:
            immovableNodes.add((x, y))
        nodesSortedAvailCapacity.append((x, y))

    nodesSortedAvailCapacity.sort(key=lambda x: -nodes[x].avail)

    curGoalNode = (maxX, 0)
    goalDataVol = nodes[curGoalNode].used
    numCommands = 0

    while curGoalNode != (0, 0):
        curNodeX, curNodeY = curGoalNode

        # If node in front of Goal node is empty, move Goal node ahead
        nodeAheadOfGoal = (curNodeX-1, curNodeY)
        if goalDataVol <= nodes[nodeAheadOfGoal].avail:
            nodes[curGoalNode].used -= goalDataVol
            nodes[curGoalNode].avail += goalDataVol
            nodes[nodeAheadOfGoal].used += goalDataVol
            nodes[nodeAheadOfGoal].avail -= goalDataVol
            curGoalNode = nodeAheadOfGoal
            numCommands += 1
            continue

        # Identify current Source and Sink nodes
        # Source node: nodeAheadOfGoal
        sourceNode = nodeAheadOfGoal
        nodesSortedAvailCapacity.sort(key=lambda x: -nodes[x].avail)
        sinkNode = nodesSortedAvailCapacity[0]

        # BFS to find path from Source node to Sink node
        path = []
        q = deque([[sourceNode, [sourceNode]]])
        seen = set()
        while q:
            (ccurNodeX, ccurNodeY), curPath = q.popleft()

            if (ccurNodeX, ccurNodeY) == sinkNode:
                path = curPath
                break

            for xOffset, yOffset in dirs:
                nextX, nextY = xOffset+ccurNodeX, yOffset+ccurNodeY
                # Next node must be:
                # - within grid
                # - not the current Goal node
                # - not previously seen in this BFS search
                # - not an "immovable node" (very large amount of data)
                if 0 <= nextX <= maxX and 0 <= nextY <= maxY and (nextX, nextY) != (curNodeX, curNodeY) and (nextX, nextY) not in seen.union(immovableNodes):
                    seen.add((nextX, nextY))
                    nextPath = list(curPath)
                    nextPath.append((nextX, nextY))
                    q.append([(nextX, nextY), nextPath])

        if len(path) < 2:
            raise AssertionError("Length of `path` should be > 1.")

        # This inplementation below focuses on performance of overall algo with regards to the desired output according to the problem statement.
        nodes[path[0]].avail += goalDataVol
        nodes[path[0]].used -= goalDataVol
        nodes[path[-1]].avail -= goalDataVol
        nodes[path[-1]].used += goalDataVol

        numCommands += len(path)-1

    print(numCommands)


if __name__ == "__main__":
    main()
