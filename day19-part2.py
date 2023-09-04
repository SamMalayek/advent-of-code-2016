
def main():
    numElves = int(open('day19.txt', 'r').read().rstrip())

    elvesToPresents = {num+1: 1 for num in range(numElves)}  # numElf -> numPresents
    elvesPlacement = [num+1 for num in range(numElves)]  # index (placement at table) -> numElf

    curElfPlacement = 0  # index of elvesPlacement
    while len(elvesPlacement) > 1:
        oppositeElfPlacement = (curElfPlacement + len(elvesPlacement)//2) % len(elvesPlacement)

        curElfNum = elvesPlacement[curElfPlacement]

        oppositeElfNum = elvesPlacement[oppositeElfPlacement]
        elvesToPresents[curElfNum] += elvesToPresents[oppositeElfNum]

        # Remove opposite elf from table
        elvesPlacement.pop(oppositeElfPlacement)
        elvesToPresents.pop(oppositeElfNum)

        # By popping to the left of curElfPlacement, our current index for
        # curElfPlacement is already moved one to the right
        if oppositeElfPlacement < curElfPlacement and curElfPlacement < len(elvesPlacement):
            continue

        # (curElfPlacement + 1) % len(elvesPlacement) <-- could create a
        # situation where curElfPlacement already equals the length
        # of the newly popped array (decreased in size), then adds
        # one to increment the index to 1 rather than 0
        if curElfPlacement >= len(elvesPlacement) - 1:
            curElfPlacement = 0
        else:
            curElfPlacement += 1

    print(list(elvesToPresents.keys())[0])


if __name__ == "__main__":
    main()
