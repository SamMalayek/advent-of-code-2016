
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
    register = {'a': 7}

    def isDigit(n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    def toggle(i, cmd):
        if i in toggleIndexes:
            numToggles = toggleIndexes[i]
            while numToggles > 0:
                cmd = toggles[cmd]
                numToggles -= 1
        return cmd

    i = 0
    while i < len(raw):
        parts = raw[i].split()
        cmd = parts[0]
        cmd = toggle(i, cmd)
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
                if (isDigit(parts[1]) and int(parts[1]) != 0) or register[parts[1]] != 0:
                    i += (int(parts[2]) if isDigit(parts[2]) else register[parts[2]])
                    continue
                else:
                    i += 1
                    continue

        else:
            if cmd == 'inc':
                register[parts[1]] += 1
            elif cmd == 'dec':
                register[parts[1]] -= 1
            elif cmd == 'tgl':
                if i+int(register[parts[1]]) in toggleIndexes:
                    toggleIndexes[i+int(register[parts[1]])] += 1
                else:
                    toggleIndexes[i+int(register[parts[1]])] = 1

        i += 1

    print(register['a'])


if __name__ == "__main__":
    main()
