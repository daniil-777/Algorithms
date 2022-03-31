def addition_upto_palindrome(line: object) -> object:
    for i in range(len(line)):
        t = line[:i] + line[::-1]
        if t == t[::-1]:
            break

    for j in reversed(range(len(line))):
        t = line[::-1] + line[j:]
        if t == t[::-1]:
            break
    return min(i, len(line) - j)
    pass


if __name__ == "__main__":
    a = addition_upto_palindrome('abc')
    print(a)
