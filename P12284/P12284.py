
from yogi import *
from itertools import islice

def read_and_count_words(n:int) -> dict[str, int]:
    words: dict[str, int] = {}
    for _ in range(n):
        x = read(str)
        if x in words:
            words[x] += 1
        else:
            words[x] = 1
    return words

def print_highest(k: int, words: list[tuple[int, int]]) -> None:
    for (_, w) in islice(words, k):
        print(w)
    print("-" * 10)

while True:
    n = scan(int)
    if not n: break
    k = read(int)
    words = read_and_count_words(n)
    top_words = sorted((-freq, w) for w, freq in words.items())
    print_highest(k, top_words)    
