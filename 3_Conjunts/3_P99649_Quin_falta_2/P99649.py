from yogi import *


def find_missing(n: int):
    k = read(int)
    all = set(range(1, n + 1))
    seen = set(read(int) for _ in range(k))
    return (all - seen).pop()


for n in tokens(int):
    print(find_missing(n))
