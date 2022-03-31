import sys
from collections import Counter


def main():
    letter_count = Counter("".join(sys.stdin.read().split()))
    keys = sorted(letter_count)
    max_number = 0
    for key in keys:
        if max_number < letter_count[key]:
            max_number = letter_count[key]
    out = []
    for i in range(max_number, 0, -1):
        for key in keys:
            if letter_count[key] >= i:
                out.append('#')
            else:
                out.append(' ')
        out.append('\n')
    out.extend(keys)
    print("".join(out))


if __name__ == '__main__':
    main()
