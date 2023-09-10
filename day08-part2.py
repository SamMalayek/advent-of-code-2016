import re


def main():
	raw = open('day08.txt', 'r').read().splitlines()

	cmds = []
	for line in raw:
		cmds.append(re.split(' |=|x|y', line))

	rect = [['.'] * 50 for _ in range(6)]

	for cmd in cmds:
		if cmd[0] == 'rect':
			cols = int(cmd[1])
			rows = int(cmd[2])
			for row in range(rows):
				for col in range(cols):
					rect[row][col] = '#'
		else:  # rotate
			if cmd[1] == 'column':
				newCol = ['.'] * len(rect)
				targetCol = int(cmd[4])
				targetMove = int(cmd[7])
				for row in range(len(rect)):
					newCol[(row + targetMove) % len(rect)] = rect[row][targetCol]

				for row in range(len(rect)):
					rect[row][targetCol] = newCol[row]

			else:  # row
				newRow = ['.'] * len(rect[0])
				targetRow = int(cmd[4])
				targetMove = int(cmd[7])
				for col in range(len(rect[0])):
					newRow[(col + targetMove) % len(rect[0])] = rect[targetRow][col]

				for col in range(len(rect[0])):
					rect[targetRow][col] = newRow[col]

	for row in rect:
		print(''.join(row))
	print(' ')


if __name__ == "__main__":
	main()
