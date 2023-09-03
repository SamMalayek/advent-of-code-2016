import re


def main():
	raw = open('day09.txt', 'r').read().rstrip()

	resp = ''
	curRaw = raw
	curMarker = list(filter(None, re.split('\)|\(|x', curRaw, maxsplit=3)))
	while curMarker:
		if len(curMarker) > 3 and not curMarker[0].isnumeric():
			resp += curMarker[0]
			curMarker = curMarker[1:]
		if len(curMarker) > 2:
			curLen = int(curMarker[0])
			curMulti = int(curMarker[1])
			resp += curMarker[2][:curLen] * curMulti
			curMarker = curMarker[2][curLen:]
		if len(curMarker) == 1:
			resp += curMarker[0]
			break

		curMarker = list(filter(None, re.split('\)|\(|x', curMarker, maxsplit=3)))

	print(len(resp))


if __name__ == "__main__":
	main()
