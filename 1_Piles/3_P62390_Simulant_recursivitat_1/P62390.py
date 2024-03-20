from yogi import *

def escriu(n: int) -> None:
    S = list[int]()
    S.append(n)
    while len(S) > 0:
        t = S.pop()
        if t > 0:
            print(f" {t}", end='')
            S.append(t-1)
            S.append(t-1)

for n in tokens(int):
    escriu(n)
    print("")
