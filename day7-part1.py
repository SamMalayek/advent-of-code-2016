import re


def followsPattern(string):
	for i in range(len(string)):
		if i+4 <= len(string) and string[i:i+2] == string[i+2:i+4][::-1] and string[i+1:i+3] != string[i]+string[i+3]:
			return True
	return False


def main():
	raw = open('input.txt', 'r').read().splitlines()

	resp = 0
	for address in raw:
		parts = re.split(']|\[', address)
		found = False
		for i, part in enumerate(parts):
			if followsPattern(part):
				if i % 2 == 0:
					found = True
				else:
					found = False
					break
		if found:
			resp += 1

	print(resp)


if __name__ == "__main__":
	main()
