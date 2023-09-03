
def main():
    puzzleInput = open('day18.txt', 'r').read().rstrip()

    grid = [list(puzzleInput)]

    numSafeTiles = sum([1 for c in grid[0] if c == '.'])

    for i in range(1, 40):
        curRow = grid[i-1]
        newRow = [''] * len(grid[0])
        for j in range(len(curRow)):
            left = curRow[j-1] if j > 0 else '.'
            center = curRow[j]
            right = curRow[j+1] if j < len(curRow)-1 else '.'

            curCell = '.'
            if left == '^' and center == '^' and right == '.':
                curCell = '^'
            elif center == '^' and right == '^' and left == '.':
                curCell = '^'
            elif left == '^' and center == '.' and right == '.':
                curCell = '^'
            elif right == '^' and center == '.' and left == '.':
                curCell = '^'

            newRow[j] = curCell
            numSafeTiles += (curCell == '.')
        grid.append(newRow)

    print(numSafeTiles)


if __name__ == "__main__":
    main()
