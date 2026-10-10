import sys
from math import isqrt


def main():
    n, k = map(int, sys.stdin.read().split())
    # максимальное m, для которого m * (m + 1) / 2 <= k
    m = (isqrt(8 * k + 1) - 1) // 2
    print(min(n, m))


if __name__ == "__main__":
    main()
