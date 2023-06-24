def main():
	raw = open('day03.txt', 'r').read().splitlines()

	parsed = [list(map(int, line.split())) for line in raw]

	resp = 0

	for i in range(0, len(parsed), 3):
		l1 = parsed[i]
		l2 = parsed[i+1]
		l3 = parsed[i+2]
		t1 = sorted([l1[0], l2[0], l3[0]])
		t2 = sorted([l1[1], l2[1], l3[1]])
		t3 = sorted([l1[2], l2[2], l3[2]])
		if sum(t1[:2]) > t1[-1]:
			resp += 1
		if sum(t2[:2]) > t2[-1]:
			resp += 1
		if sum(t3[:2]) > t3[-1]:
			resp += 1

	print(resp)


if __name__ == "__main__":
	main()
