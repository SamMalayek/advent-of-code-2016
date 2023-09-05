
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

    if ips[0][0] == 0:
        print(ips[0][1]+1)
    else:
        print(0)


if __name__ == "__main__":
    main()
