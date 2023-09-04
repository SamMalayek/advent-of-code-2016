
def main():
    numElves = int(open('day19.txt', 'r').read().rstrip())

    elvesToNumPresents = [1 for _ in range(numElves)]

    maxPresentsForOneElf = 1

    curElf = 0
    while maxPresentsForOneElf < numElves:
        if elvesToNumPresents[curElf] > 0:
            nextElf = (curElf + 1) % numElves
            while elvesToNumPresents[nextElf] == 0:
                nextElf = (nextElf + 1) % numElves
            elvesToNumPresents[curElf] += elvesToNumPresents[nextElf]
            elvesToNumPresents[nextElf] = 0

            maxPresentsForOneElf = max(maxPresentsForOneElf, elvesToNumPresents[curElf])
            if maxPresentsForOneElf != numElves:
                curElf = nextElf
        else:
            curElf = (curElf + 1) % numElves

    print(curElf+1)


if __name__ == "__main__":
    main()
