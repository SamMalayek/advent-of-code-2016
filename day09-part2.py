import re


def main():
	raw = open('day09.txt', 'r').read().rstrip()

	def recurse(cur):
		resp = ''
		curMarker = re.split('\)|\(|x', cur, maxsplit=3)
		while curMarker:
			if len(curMarker) > 2:
				if not curMarker[0].isnumeric():
					resp += curMarker[0]
					curMarker = curMarker[1:]
					continue
				curLen = int(curMarker[0])
				curMulti = int(curMarker[1])
				resp += recurse(curMarker[2][:curLen]) * curMulti

				curMarker = re.split('\)|\(|x', curMarker[2][curLen:], maxsplit=3)
			else:
				return resp + ''.join(curMarker)

		return resp

	print(len(recurse(raw)))


if __name__ == "__main__":
	main()
