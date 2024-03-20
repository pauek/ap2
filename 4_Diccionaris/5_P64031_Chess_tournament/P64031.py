from yogi import *

results: dict[str, tuple[int, int, int]] = {}

def update(player: str, t: tuple[int, int, int]):
    wins, draws, defeats = results[player]
    results[player] = (wins + t[0], draws + t[1], defeats + t[2])

def read_players():
    n = read(int)
    for _ in range(n):
        name = read(str)
        results[name] = (0, 0, 0)

def read_games():
    while True:
        p1 = scan(str)
        if not p1:
            break
        p2 = read(str)
        result = read(str)
        if result == "1-0":
            update(p1, (1, 0, 0))
            update(p2, (0, 0, 1))
        elif result == "0-1":
            update(p1, (0, 0, 1))
            update(p2, (1, 0, 0))
        elif result == "1/2-1/2":
            update(p1, (0, 1, 0))
            update(p2, (0, 1, 0))

def show_results():
    for player, res in sorted(results.items()):
        print(f"{player} {res[0]} {res[1]} {res[2]}")
    

read_players()
read_games()
show_results()

