from yogi import *

def escriu(n: int) -> None:
    S = list[tuple[str, int]]()
    S.append(("expand", n))
    while len(S) > 0:
        what, n = S.pop()
        if what == "expand":
            if n > 1:
                S.append(("expand", n - 1))
                S.append(("write", n))
                S.append(("expand", n - 1))
            else:
                S.append(("write", 1))
        elif what == "write":
            print(f" {n}", end='')

for n in tokens(int):
    escriu(n)
    print("")
