import sys


def git_log(line):
    line1 = line[0:7]
    j = 0
    i = 7
    while (j < 4):
        if line[i] == '\t':
            j += 1
        i += 1
    line2 = line[i:len(line) - 1]
    line3 = '.' * (73 - len(line2))
    answer = '{0}{1}{2}'.format(line1, line3, line2)
    print(answer)


def sol(str):
    first = str.split('\t')
    second = first[0][:7]
    third = first[-1].rstrip("\r\n")
    dot = '.' * (73 - len(third))
    print('{0}{1}{2}'.format(second, dot, third))


if __name__ == '__main__':
    for string in sys.stdin:
        sol(string)
