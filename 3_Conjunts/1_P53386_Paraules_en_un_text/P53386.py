import yogi

wordset = set()

for word in yogi.tokens(str):
    wordset.add(word.lower())

for word in sorted(wordset):
    print(word)