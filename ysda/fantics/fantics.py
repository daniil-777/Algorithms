from typing import Set


def get_combinations(fantics_num: int, coins_nominals: Set[int]) -> int:
    ways = [0] * (fantics_num + 1)
    ways[0] = 1
    for coin in coins_nominals:
        for j in range(coin, fantics_num + 1):
            ways[j] +=  ways[j - coin]
    return ways[fantics_num]
