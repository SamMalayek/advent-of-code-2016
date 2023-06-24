def main():
	raw = open('day02.txt', 'r').read().splitlines()

	keypad = [
		['1', '2', '3'],
		['4', '5', '6'],
		['7', '8', '9'],
	]

	dirs = {  # row, col
		'U': (-1, 0),
		'D': (1, 0),
		'L': (0, -1),
		'R': (0, 1),
	}

	row, col = 1, 1

	resp = ''

	for line in raw:
		for d in line:
			row += dirs[d][0]
			col += dirs[d][1]

			row = min(len(keypad)-1, row)
			row = max(0, row)
			col = min(len(keypad[0])-1, col)
			col = max(0, col)
		resp += keypad[row][col]

	print(resp)


if __name__ == "__main__":
	main()
