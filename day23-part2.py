
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

    def isDigit(n):
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
        cmd = parts[0]
        cmd = toggle(i, cmd)
        if cmd == 'cpy':  # num, registerNum
            if isDigit(parts[2]):
                i += 1
                continue
            if isDigit(parts[1]):
                register[parts[2]] = int(parts[1])
            else:
                register[parts[2]] = register[parts[1]]
        elif cmd == 'inc':
            register[parts[1]] += 1
        elif cmd == 'dec':
            register[parts[1]] -= 1
        elif cmd == 'tgl':
            numberOfToggles += 1
            toggleIndexes[i+register[parts[1]]] = True
        elif cmd == 'jnz':  # num, registerNum
            val1 = int(parts[1]) if isDigit(parts[1]) else register[parts[1]]
            val2 = int(parts[2]) if isDigit(parts[2]) else register[parts[2]]
            if i in jumpStates and val1 != 0 and val2 < 0:
                aa, bb, cc, dd, numT = jumpStates[i]
                if numT != numberOfToggles:
                    jumpStates[i] = (register['a'], register['b'], register['c'], register['d'], numberOfToggles)
                    i += val2
                    continue
                else:
                    numIterations = abs(val1)
                    register['a'] += (register['a'] - aa)*numIterations
                    register['b'] += (register['b'] - bb)*numIterations
                    register['c'] += (register['c'] - cc)*numIterations
                    register['d'] += (register['d'] - dd)*numIterations
                    jumpStates[i] = (register['a'], register['b'], register['c'], register['d'], -1)
                    i += 1
                    continue
            elif val1 != 0:
                jumpStates[i] = (register['a'], register['b'], register['c'], register['d'], numberOfToggles)
                i += val2
                continue
            else:
                jumpStates[i] = (register['a'], register['b'], register['c'], register['d'], numberOfToggles)
                i += 1
                continue

        i += 1

    print(register['a']+2)


if __name__ == "__main__":
    main()
