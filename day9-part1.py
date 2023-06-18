import re


def main():
	raw = open('input.txt', 'r').read().rstrip()

	resp = ''
	curRaw = raw
	curMarker = list(filter(None, re.split('\)|\(|x', curRaw, maxsplit=3)))
	while curMarker:
		if len(curMarker) > 2:
			curLen = int(curMarker[0])
			curMulti = int(curMarker[1])
			resp += curMarker[2][:curLen] * curMulti
			curMarker = curMarker[2][curLen:]

		curMarker = list(filter(None, re.split('\)|\(|x', curMarker, maxsplit=3)))

	print(len(resp))


if __name__ == "__main__":
	main()
