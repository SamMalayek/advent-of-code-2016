
def main():
    raw = open('day23.txt', 'r').read().splitlines()
    toggleIndexes = {}  # line number (indexed at 0) -> num toggles
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
<<<<<<< Updated upstream
        if len(parts) > 2:
            if cmd == 'cpy':  # num, registerNum
                if isDigit(parts[2]):
                    i += 1
                    continue
                if isDigit(parts[1]):
                    register[parts[2]] = int(parts[1])
                else:
                    register[parts[2]] = register[parts[1]]
            elif cmd == 'jnz':  # num, registerNum
                # We're going to mutate the input array, replacing the iteration with addition/multiplication. 
                # NOTE: can be improved by handling nested jumps ->> releasing tomorrow.
                if isDigit(parts[2]) and int(parts[2]) < 0:
                    targetRegKey = parts[1]
                    lookBack = int(parts[2])
                    incs = set()
                    decs = set()
                    skipOptimization = False
                    for j in range(i+lookBack, i):
                        pparts = raw[j].split()
                        if pparts[0] not in {'dec', 'inc'}:
                            skipOptimization = True
                            break
                        cmd = toggle(j, pparts[0])
                        if cmd == 'dec':
                            decs.add(pparts[1])
                        elif cmd == 'inc':
                            incs.add(pparts[1])
                    if not skipOptimization:
                        targetRegKeyCount = abs(register[targetRegKey])
                        for inc in incs:
                            register[inc] += targetRegKeyCount
                        for dec in decs:
                            register[dec] -= targetRegKeyCount
                        i += 1
                        continue

                if (isDigit(parts[1]) and int(parts[1]) != 0) or register[parts[1]] != 0:
=======
        if cmd == 'cpy':  # num, registerNum
            if isDigit(parts[2]):
                i += 1
                continue
            if isDigit(parts[1]):
                register[parts[2]] = int(parts[1])
            else:
                register[parts[2]] = register[parts[1]]
        elif cmd == 'jnz':  # num, registerNum
            if i in jumpStates and ((isDigit(parts[1]) and int(parts[1]) != 0) or (register[parts[1]]) != 0) and ((isDigit(parts[2]) and int(parts[2]) < 0) or (register[parts[2]]) < 0):
                aa, bb, cc, dd, numT = jumpStates[i]
                if numT != numberOfToggles:
                    jumpStates[i] = (register['a'], register['b'], register['c'], register['d'], numberOfToggles)
>>>>>>> Stashed changes
                    i += (int(parts[2]) if isDigit(parts[2]) else register[parts[2]])
                    continue
                else:
                    numIterations = abs(int(parts[1]) if isDigit(parts[1]) else register[parts[1]])
                    register['a'] += (register['a'] - aa)*numIterations
                    register['b'] += (register['b'] - bb)*numIterations
                    register['c'] += (register['c'] - cc)*numIterations
                    register['d'] += (register['d'] - dd)*numIterations
                    jumpStates[i] = (register['a'], register['b'], register['c'], register['d'], -1)
                    i += 1
                    continue
            elif ((isDigit(parts[1]) and int(parts[1]) != 0) or (register[parts[1]]) != 0):
                jumpStates[i] = (register['a'], register['b'], register['c'], register['d'], numberOfToggles)
                i += (int(parts[2]) if isDigit(parts[2]) else register[parts[2]])
                continue
            else:
                jumpStates[i] = (register['a'], register['b'], register['c'], register['d'], numberOfToggles)
                i += 1
                continue
        if cmd == 'inc':
            register[parts[1]] += 1
        elif cmd == 'dec':
            register[parts[1]] -= 1
        elif cmd == 'tgl':
            numberOfToggles += 1
            if i+register[parts[1]] in toggleIndexes:
                toggleIndexes[i+register[parts[1]]] += 1
            else:
                toggleIndexes[i+register[parts[1]]] = 1

        i += 1

    print(register['a']+2)


if __name__ == "__main__":
    main()
