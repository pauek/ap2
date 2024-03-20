from yogi import *

D: dict[str, int] = {}
for w in map(lambda w: w.lower(), tokens(str)):
    D[w] = D[w]+1 if w in D else 1
 
for word, freq in sorted(D.items()):
    print(word, freq)
