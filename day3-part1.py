def main():
	raw = open('input.txt', 'r').read().splitlines()

	parsed = [list(map(int, line.split())) for line in raw]

	resp = 0

	for line in parsed:
		line.sort()
		if sum(line[:2]) > line[-1]:
			resp += 1
	print(resp)


if __name__ == "__main__":
	main()
