from re import split

def dragonCurve(a):
    b = list(a[::-1])
    for i in range(len(b)):
        if b[i] == '1':
            b[i] = '0'
        else:  # b == '0'
            b[i] = '1'

    return a + '0' + ''.join(b)

def calcChecksum(s):
    resp = []
    for i in range(0, len(s), 2):
        if i+1 < len(s):
            resp.append('1' if s[i] == s[i+1] else '0')
    return ''.join(resp)

def main():
    puzzleInput = open('day16.txt', 'r').read().rstrip()
    diskLen = 35651584

    # First fill data with dragon curve until we reach the disk len:
    while len(puzzleInput) < diskLen:
        puzzleInput = dragonCurve(puzzleInput)

    # Truncate to disk size
    puzzleInput = puzzleInput[:diskLen]

    # Then calculate the checksum until it's odd len:
    checksum = calcChecksum(puzzleInput)

    while len(checksum) % 2 == 0:
        checksum = calcChecksum(checksum)

    print(checksum)

if __name__ == "__main__":
    main()
