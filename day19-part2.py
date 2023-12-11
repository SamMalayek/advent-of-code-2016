from collections import deque


def main():
    numElves = int(open('day19.txt', 'r').read().rstrip())

    # Disclaimer: This updated solution was inspired from
    # https://www.reddit.com/r/adventofcode/comments/5j4lp1/2016_day_19_solutions/dbdf9mn/
    # I prefer the small modifications in this one.

    left = deque()
    right = deque()

    for i in range(1, numElves + 1):
        if len(left) < numElves // 2 + 1:  # Left needs to be bigger.
            left.append(i)  # Example: 1 to 11
        else:
            right.append(i)  # Example: 12 to 20

    while right:
        if len(left) > len(right):  # The middle of the circle is the end of `left` or beginning of `right`.
            left.pop()
        else:
            right.popleft()

        # Rotate the cut in the circle to move 'the middle' in accordance with the problem statement.
        right.append(left.popleft())
        left.append(right.popleft())

    print(left[0])


if __name__ == "__main__":
    main()
