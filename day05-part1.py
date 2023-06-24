from hashlib import md5


def main():
	puzzleInput = open('day05.txt', 'r').read().rstrip()

	i = 0
	resp = ''
	while True:
		curPreHash = puzzleInput + str(i)
		curHash = md5(curPreHash.encode('utf-8')).hexdigest()
		if curHash[:5] == '00000':
			resp += curHash[5]

			if len(resp) == 8:
				print(resp)
				exit()
		i += 1


if __name__ == "__main__":
	main()
