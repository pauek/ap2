from yogi import *


def read_social_net() -> list[set[int]]:
    n, m = read(int), read(int)
    net = [set[int]() for _ in range(n)]
    for _ in range(m):
        a, b = read(int), read(int)
        net[a].add(b)
        net[b].add(a)
    return net


def friends_of_friends(net: list[set[int]], i: int) -> set[int]:
    frs = net[i]
    frs_of_frs = frs.copy()
    for f in frs:
        frs_of_frs |= net[f]
    frs_of_frs.discard(i)
    return frs_of_frs


net = read_social_net()
for i in tokens(int):
    print(len(friends_of_friends(net, i)))
