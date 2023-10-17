
class Node:
    def __init__(self, path, used=0, avail=0):
        self.path = path
        self.used = used  # in Terabytes
        self.avail = avail


def main():
    raw = open('day22.txt', 'r').read().splitlines()

    nodes = []

    for line in raw[2:]:
        path, _, used, avail, _ = line.split()
        nodes.append(Node(path, int(used[:-1]), int(avail[:-1])))

    seen = set()

    for n1 in nodes:
        for n2 in nodes:
            if n1.path == n2.path:
                continue
            if 0 < n1.used <= n2.avail or 0 < n2.used <= n1.avail:
                curPair = sorted([n1.path, n2.path])
                seen.add(tuple(curPair))
    print(len(seen))


if __name__ == "__main__":
    main()



