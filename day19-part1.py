
def main():
    numElves = int(open('day19.txt', 'r').read().rstrip())

    # Explanation for the magic below on Numberphile: https://www.youtube.com/watch?v=uCsD3ZGzMgE

    numElvesBin = bin(numElves)[2:]

    winningPosBin = numElvesBin[1:] + numElvesBin[0]

    print(int(winningPosBin, 2))


if __name__ == "__main__":
    main()
