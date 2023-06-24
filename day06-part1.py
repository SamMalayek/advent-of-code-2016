from collections import Counter


def main():
	raw = open('day06.txt', 'r').read().splitlines()

	resp = ''

	for i in range(len(raw[0])):
		counter = Counter()
		for j in range(len(raw)):
			cur = raw[j][i]
			counter[cur] += 1
		resp += counter.most_common()[0][0]

	print(resp)


if __name__ == "__main__":
	main()
