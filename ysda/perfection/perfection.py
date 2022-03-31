def is_perfect(n):
    s = [j for j in range(1, n // 2 + 1) if not n % j]
    return sum(s) == n
