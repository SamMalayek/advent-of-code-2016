from collections import Counter


def main():
	raw = open('day04.txt', 'r').read().splitlines()

	for line in raw:
		name, checksum = line.split('[')
		sector = int(name[-3:])
		name = name[:-3].replace('-', '')
		counts = sorted(Counter(name).most_common(), key=lambda x: ord(x[0])-(x[1]*100))

		good = True
		for i in range(5):
			if counts[i][0] != checksum[i]:
				good = False
				break

		if good:
			res = ''
			for c in name:
				o = (ord(c) - 97 + sector) % 26
				res += chr(o + 97)
			if 'northpole' in res:
				print(sector)


if __name__ == "__main__":
	main()
