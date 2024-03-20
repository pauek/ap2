from yogi import *

D: dict[str, int] = {}
for word in tokens(str):
    lower = word.lower()
    if lower in D:
        D[lower] += 1
    else:
        D[lower] = 1
    
for word in sorted(D):
    print(word, D[word])
