import re


def followsPattern(string, isAba, seen):
	for i in range(len(string)):
		if i+2 < len(string) and string[i] == string[i+2] and string[i] != string[i+1]:
			seen.add((string[i], string[i+1]) if isAba else (string[i+1], string[i]))


def main():
	raw = open('input.txt', 'r').read().splitlines()

	resp = 0
	for address in raw:
		parts = re.split(']|\[', address)
		seenAba = set()
		seenBab = set()
		for i, part in enumerate(parts):
			if i % 2 == 0:
				followsPattern(part, True, seenAba)
			else:
				followsPattern(part, False, seenBab)

		if seenAba.intersection(seenBab):
			resp += 1

	print(resp)


if __name__ == "__main__":
	main()
