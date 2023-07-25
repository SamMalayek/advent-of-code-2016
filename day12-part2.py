from collections import defaultdict


def main():
	raw = open('day12.txt', 'r').read().splitlines()
	instructions = [list(map(lambda c: int(c) if c.lstrip('-').isnumeric() else c, line.split(' '))) for line in raw]
	register = defaultdict(int)
	register['c'] = 1

	cur = 0

	while cur < len(instructions):
		parts = instructions[cur]
		operator = parts[0]
		x = parts[1]
		y = parts[2] if len(parts) > 2 else None

		if operator == 'cpy':
			if type(x) == int:
				register[y] = x
			else:
				register[y] = register[x]
		elif operator == 'inc':
			register[x] += 1
		elif operator == 'dec':
			register[x] -= 1
		elif operator == 'jnz':
			if (type(x) == int and x != 0) or register[x] != 0:
				cur += y
				continue
		else:
			raise NotImplementedError(f'Operator: `{operator}` not implemented.')

		cur += 1
	print(register['a'])


if __name__ == "__main__":
	main()
