import random


def quick_sort(data):
    if len(data) == 0 or len(data) == 1:
        return data
    i = random.randint(0, len(data) - 1)
    pivot = data[i]
    less = [el for el in data if el < pivot]
    more = [el for el in data if el > pivot]
    return quick_sort(less) + [x for x in data if x == pivot] + quick_sort(more)


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    print(' '.join(map(str, quick_sort(data))))
