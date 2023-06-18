from hashlib import md5


def main():
	puzzleInput = open('input.txt', 'r').read().rstrip()

	i = 0
	resp = [0 for _ in range(8)]
	seen = set()
	while True:
		curPreHash = puzzleInput + str(i)
		curHash = md5(curPreHash.encode('utf-8')).hexdigest()
		if curHash[:5] == '00000' and curHash[5].isnumeric() and int(curHash[5]) < 8 and int(curHash[5]) not in seen:
			resp[int(curHash[5])] = curHash[6]
			seen.add(int(curHash[5]))
			if len(seen) == 8:
				print(''.join(resp))
				exit()
		i += 1


if __name__ == "__main__":
	main()
