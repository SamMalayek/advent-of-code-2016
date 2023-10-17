
class AocException(Exception):
    pass


def main():
    raw = open('day25.txt', 'r').read().splitlines()
    toggles = {
        'inc': 'dec',
        'dec': 'inc',
        'jnz': 'cpy',
        'tgl': 'inc',
        'cpy': 'jnz'
        # default 1: inc
        # default 2: jnz
    }

    def isDigit(n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    def toggle(i, cmd, toggleIndexes):
        if i in toggleIndexes:
            cmd = toggles[cmd]
        return cmd

    def handleOutResp(outRespExp, outRespC, n, j):
        if outRespExp != n:
            raise AocException()
        outRespExp = 1 if outRespExp == 0 else 0
        outRespC += 1
        if outRespC == 50:
            print(j)
            quit()
        return outRespExp, outRespC

    j = 0
    while j < 1000:
        register = {'a': j, 'b': 0, 'c': 0, 'd': 0}
        outRespExpectation = 0
        outRespCount = 0
        toggleIndexes = {}  # line number (indexed at 0) -> bool
        i = 0
        while i < len(raw):
            parts = raw[i].split()
            cmd = toggle(i, parts[0], toggleIndexes)

            if cmd == 'cpy':  # num, registerNum
                if isDigit(parts[2]):
                    i += 1
                    continue
                if isDigit(parts[1]):
                    register[parts[2]] = int(parts[1])
                else:
                    register[parts[2]] = register[parts[1]]
            elif cmd == 'out':
                val1 = int(parts[1]) if isDigit(parts[1]) else register[parts[1]]
                try:
                    outRespExpectation, outRespCount = handleOutResp(outRespExpectation, outRespCount, val1, j)
                except AocException:
                    j += 1
                    break
            elif cmd == 'jnz':  # num, registerNum
                val1 = int(parts[1]) if isDigit(parts[1]) else register[parts[1]]
                if val1 != 0:
                    i += (int(parts[2]) if isDigit(parts[2]) else register[parts[2]])
                    continue
                else:
                    i += 1
                    continue
            elif cmd == 'inc':
                register[parts[1]] += 1
            elif cmd == 'dec':
                register[parts[1]] -= 1
            elif cmd == 'tgl':
                toggleIndexes[i+int(register[parts[1]])] = True

            i += 1


if __name__ == "__main__":
    main()
