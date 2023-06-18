def main():
	raw = open('input.txt', 'r').read().rstrip()

	curDir = {  # x, y
		'D': (0, -1),
		'R': (1, 0),
		'L': (-1, 0),
		'U': (0, 1),
	}

	dirs = {
		'R': {
			'R': 'D',
			'L': 'U',
		},
		'D': {
			'R': 'L',
			'L': 'R',
		},
		'U': {
			'R': 'R',
			'L': 'L',
		},
		'L': {
			'R': 'U',
			'L': 'D',
		}
	}

	parsed = raw.split(', ')

	x, y = 0, 0

	d = 'U'

	for instruction in parsed:
		turn = instruction[:1]
		steps = int(instruction[1:])

		newD = dirs[d][turn]

		while steps > 0:
			x += curDir[newD][0]
			y += curDir[newD][1]
			steps -= 1

		d = newD

	print(abs(x) + abs(y))


if __name__ == "__main__":
	main()
