from hashlib import md5
from collections import deque

def main():
    puzzleInput = open('day17.txt', 'r').read().rstrip()
    doorOpen = {'b', 'c', 'd', 'e', 'f'}
    hashIndex = {
        (1, 0): 1,
        (0, 1): 3,
        (-1, 0): 0,
        (0, -1): 2
    }
    dirs = {
        (1, 0): 'D',
        (0, 1): 'R',
        (-1, 0): 'U',
        (0, -1): 'L'
    }

    def getHash(pathToCur):
        toHash = puzzleInput + ''.join(pathToCur)
        curHash = md5(toHash.encode('utf-8')).hexdigest()
        return curHash[:4]

    curArgs = ((0, 0), [])  # curPos, pathToCur

    q = deque([curArgs])

    while q:
        curPos, pathToCur = q.popleft()

        if curPos == (3, 3):
            print(''.join(pathToCur))
            exit()

        curRow, curCol = curPos[0], curPos[1]
        curHash = getHash(pathToCur)

        for rowOffset, colOffset in dirs.keys():
            nextRow, nextCol = rowOffset+curRow, colOffset+curCol

            nextPosOffset = (rowOffset, colOffset)

            if 0 <= nextRow <= 3 and 0 <= nextCol <= 3:

                if curHash[hashIndex[nextPosOffset]] not in doorOpen:
                    continue

                pathToNext = list(pathToCur)
                pathToNext.append(dirs[nextPosOffset])

                q.append(((nextRow, nextCol), pathToNext))


if __name__ == "__main__":
    main()
