import sys


def counter(arguments, text):
    answ = ''
    if '-l' in arguments:
        answ += str(len(text)) + " "
    if '-w' in arguments:
        num = without_keys.replace('\n', ' ')
        num = num.replace('\t', ' ')
        num = list(filter(None, num.split(" ")))
        answ += str(len(num)) + " "
    if '-m' in arguments:
        answ += str(len(without_keys)) + " "
    if '-L' in keys:
        max = 0
        for item in text:
            if (len(item) > max):
                max = len(item)
        answ += str(max) + " "
    answ = answ[:-1]
    print(answ)


if __name__ == '__main__':
    total = ''
    for line in sys.stdin:
        total += line
    if total.find('\n') != -1:
        keys = total[:total.find('\n')]
        without_keys = '' + total[total.find('\n') + 1:]
    else:
        keys = total
        without_keys = ''

    arguments = tuple(keys.split(" "))
    text = without_keys.split('\n')
    if text[-1] == "":
        text = text[:-1]
    counter(arguments, text)
