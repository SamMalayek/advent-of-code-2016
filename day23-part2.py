
# NOTE: This solution still needs more work to work with all possible inputs. But it is fast.
def main():
    raw = open('day23.txt', 'r').read().splitlines()
    toggleIndexes = {}  # line number (indexed at 0) -> bool
    toggles = {
        'inc': 'dec',
        'dec': 'inc',
        'jnz': 'cpy',
        'tgl': 'inc',
        'cpy': 'jnz'
        # default 1: inc
        # default 2: jnz
    }
    numberOfToggles = 0
    jumpStates = {}
    register = {'a': 12, 'b': 0, 'c': 0, 'd': 0}

    def extractVal(v):
        return int(v) if isDigit(v) else register[v]

    def getJumpStates(numToggles):
        return (register['a'], register['b'], register['c'], register['d'], numToggles)

    def isDigit(n):  # This handles negative numbers in strings, like "-3" that isnumeric() doesn't handle.
        try:
            int(n)
            return True
        except ValueError:
            return False

    def toggle(i, cmd):
        if i in toggleIndexes:
            cmd = toggles[cmd]
        return cmd

    i = 0
    while i < len(raw):
        parts = raw[i].split()
        cmd = toggle(i, parts[0])
        if cmd == 'cpy':  # num, registerNum
            if not isDigit(parts[2]):
                register[parts[2]] = extractVal(parts[1])
        elif cmd == 'inc':
            register[parts[1]] += 1
        elif cmd == 'dec':
            register[parts[1]] -= 1
        elif cmd == 'tgl':
            numberOfToggles += 1
            toggleIndexes[i+register[parts[1]]] = True
        elif cmd == 'jnz':  # num, registerNum
            val1 = extractVal(parts[1])
            val2 = extractVal(parts[2])
            if i in jumpStates and val1 != 0 and val2 < 0:
                aa, bb, cc, dd, numT = jumpStates[i]
                if numT != numberOfToggles:
                    jumpStates[i] = getJumpStates(numberOfToggles)
                    i += val2
                    continue
                else:
                    numIterations = abs(val1)
                    register['a'] += (register['a'] - aa)*numIterations
                    register['b'] += (register['b'] - bb)*numIterations
                    register['c'] += (register['c'] - cc)*numIterations
                    register['d'] += (register['d'] - dd)*numIterations
                    jumpStates[i] = getJumpStates(-1)
            elif val1 != 0:
                jumpStates[i] = getJumpStates(numberOfToggles)
                i += val2
                continue
            else:
                jumpStates[i] = getJumpStates(numberOfToggles)

        i += 1

    print(register['a']+2)


if __name__ == "__main__":
    main()
