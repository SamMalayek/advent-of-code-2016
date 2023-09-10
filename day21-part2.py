
# There's a fair bit of list<->string transformations just for the purpose of
# using APIs of that type. Not a big deal given the scope of the problem.
def main():
    raw = open('day21.txt', 'r').read().splitlines()
    scrambleInput = list('fbgdceah')

    def swapIndexes(s, x, y):
        s[x], s[y] = s[y], s[x]
        return s

    def swapLetters(s, c1, c2):
        return list(''.join(s).replace(c1, '!').replace(c2, c1).replace('!', c2))

    def rotate(s, steps, isRight):
        if not isRight:
            s = s[-steps:] + s[:-steps]
        else:
            s = s[steps:] + s[:steps]
        return s

    def rotateBasedOnPos(s, c):
        i = ''.join(s).find(c)
        reverseMap = {
            1: 1,
            3: 2,
            5: 3,
            7: 4,
            2: 6,
            4: 7,
            6: 0,
            0: 1,
        }
        return rotate(s, reverseMap[i], True)

    def reversePos(s, x, y):
        subList = s[x:y+1][::-1]
        return s[:x] + subList + s[y+1:]

    def move(s, x, y):
        s.insert(y, s.pop(x))
        return s

    for line in reversed(raw):
        parts = line.split(' ')
        if parts[0] == 'swap':
            a = parts[2]
            b = parts[5]
            if parts[1] == 'letter':
                scrambleInput = swapLetters(scrambleInput, a, b)
            else:  # position
                scrambleInput = swapIndexes(scrambleInput, int(a), int(b))
        elif parts[0] == 'move':
            a = parts[2]
            b = parts[5]
            scrambleInput = move(scrambleInput, int(b), int(a))
        elif parts[0] == 'rotate':
            if parts[1] == 'based':  # on position
                scrambleInput = rotateBasedOnPos(scrambleInput, parts[-1])
            else:  # right/left
                scrambleInput = rotate(scrambleInput, int(parts[2]), parts[1] == 'right')
        elif parts[0] == 'reverse':  # positions
            scrambleInput = reversePos(scrambleInput, int(parts[2]), int(parts[-1]))

    print(''.join(scrambleInput))


if __name__ == "__main__":
    main()
