def main():
	raw = open('input.txt', 'r').read().splitlines()

	keypad = [
		['!', '!', '1', '!', '!'],
		['!', '2', '3', '4', '!'],
		['5', '6', '7', '8', '9'],
		['!', 'A', 'B', 'C', '!'],
		['!', '!', 'D', '!', '!'],
	]

	dirs = {  # row, col
		'U': (-1, 0),
		'D': (1, 0),
		'L': (0, -1),
		'R': (0, 1),
	}

	row, col = 2, 0

	resp = ''

	for line in raw:
		for d in line:
			nRow = row + dirs[d][0]
			nCol = col + dirs[d][1]

			nRow = min(len(keypad)-1, nRow)
			nRow = max(0, nRow)
			nCol = min(len(keypad[0])-1, nCol)
			nCol = max(0, nCol)

			if keypad[nRow][nCol] != '!':
				row = nRow
				col = nCol
		resp += keypad[row][col]

	print(resp)


if __name__ == "__main__":
	main()
