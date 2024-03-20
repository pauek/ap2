from yogi import *

D: dict[str, int] = {}
for w in map(lambda w: w.lower(), tokens(str)):
    D[w] = D[w]+1 if w in D else 1

mirrored_items = ((freq, word) for word, freq in D.items())
for (freq, word) in sorted(mirrored_items):
    print(freq, word)
