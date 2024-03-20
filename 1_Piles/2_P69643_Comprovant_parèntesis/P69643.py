import sys

matching = {"(": ")", "[": "]", "{": "}"}
open_chars = matching.keys()
close_chars = matching.values()


def check_parens(line: str) -> bool:
    unpaired = list[str]()
    for ch in line:
        if ch in open_chars:
            unpaired.append(ch)
        else:
            assert ch in close_chars
            if len(unpaired) == 0:
                return False
            prev = unpaired.pop()
            if matching.get(prev) != ch:
                return False
    return len(unpaired) == 0


for line in sys.stdin:
    for word in line.strip().split(" "):
        veredict = "correcta" if check_parens(word) else "incorrecta"
        print(f"{word} es {veredict}")
