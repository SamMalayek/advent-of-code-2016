from collections import defaultdict
from hashlib import md5
from itertools import groupby


def main():
	puzzleInput = open('day14.txt', 'r').read().rstrip()
	# key: single digit representing triples, value: list of indexes. queue would be more space efficient
	triples = defaultdict(list)

	i = 0
	keys = set()

	while len(keys) < 64:
		curPreHash = puzzleInput + str(i)
		curHash = md5(curPreHash.encode('utf-8')).hexdigest()

		groups = [list(g) for k, g in groupby(curHash)]
		seenTriple = False
		for g in groups:
			if len(g) >= 3 and not seenTriple:
				triples[g[0]].append(i)
				seenTriple = True
			if len(g) >= 5:
				listIndex = 0

				while listIndex < len(triples[g[0]]):
					curTriplesIndex = triples[g[0]][listIndex]  # value of each item in list is an index

					if i - curTriplesIndex <= 1000 and i != curTriplesIndex:
						keys.add(curTriplesIndex)

					listIndex += 1

		i += 1

	print(sorted(keys)[63])


if __name__ == "__main__":
	main()
