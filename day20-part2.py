
def main():
    raw = open('day20.txt', 'r').read().splitlines()

    ips = []

    for line in raw:
        ips.append(list(map(int, line.split('-'))))
    ips.sort()

    i = 0
    while i < len(ips)-1:
        if ips[i][1] >= ips[i+1][0]-1:
            ips[i][1] = max(ips[i][1], ips[i+1][1])
            ips.pop(i+1)
            continue
        i += 1

    i = 0
    resp = (4294967295 - ips[-1][1])
    while i < len(ips) - 1:
        cur = ips[i]
        nex = ips[i+1]

        resp += (nex[0] - cur[1] - 1)
        i += 1

    print(resp)


if __name__ == "__main__":
    main()
