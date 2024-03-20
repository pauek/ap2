from yogi import *

casino: dict[str, int] = {}

def enter(person: str, casino: dict[str, int]) -> None:
    if person in casino:
        print(f"{person} is already in the casino")
    else:
        casino[person] = 0

def leave(person: str, casino: dict[str, int]) -> None:
    if person not in casino:
        print(f"{person} is not in the casino")
    else:
        print(f"{person} has won {casino[person]}")
        del casino[person]

def win(person: str, casino: dict[str,int]) -> None:
    amount = read(int)
    if person not in casino:
        print(f"{person} is not in the casino")
    else:
        casino[person] += amount

eventFuncs = {
    "enters": enter,
    "leaves": leave,
    "wins": win,
}

while True:
    person = scan(str)
    if not person:
        break
    event = read(str)
    eventFuncs[event](person, casino)
   
print("-" * 10)
for person, amount in sorted(casino.items()):
    print(f"{person} is winning {amount}")