import sys
from typing import Callable

OperatorFunc = Callable[[int, int], int]

operator_funcs: dict[str, OperatorFunc] = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
}

def apply(S: list[int], op: str) -> None:
    b, a = S.pop(), S.pop()
    S.append(operator_funcs[op](a, b))

def eval(expr: list[str]) -> int:
    S = list[int]()
    for tok in expr:
        if tok.isdigit():
            S.append(int(tok))
        else:
            apply(S, tok)
    return S[0]

for expression in sys.stdin:
    print(eval(expression.strip().split(" ")))