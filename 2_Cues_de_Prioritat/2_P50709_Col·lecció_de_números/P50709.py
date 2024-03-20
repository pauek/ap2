from yogi import tokens
from heapq import *
from typing import Callable

Heap = list[int]


def show(heap: Heap, _: int = 0) -> None:
    print(-heap[0])


def remove(heap: Heap, _: int = 0) -> None:
    heappop(heap)


def increment(heap: Heap, k: int) -> None:
    heappush(heap, -(-heappop(heap) + k))


def decrement(heap: Heap, k: int) -> None:
    heappush(heap, -(-heappop(heap) - k))


def add(heap: Heap, k: int) -> None:
    heappush(heap, -k)


HeapFunc = Callable[[Heap, int], None]
opinfo: dict[str, tuple[HeapFunc, int, bool]] = {
    "A": (show, 1, True),
    "R": (remove, 1, True),
    "S": (add, 2, False),
    "I": (increment, 2, True),
    "D": (decrement, 2, True),
}


def process_commands(cmds: list[str]):
    heap = Heap()
    pos = 0
    while pos < len(cmds):
        func, skip, check_empty = opinfo[cmds[pos]]
        if check_empty and len(heap) == 0:
            print(f"error!")
        else:
            func(heap, int(cmds[pos + 1]) if skip == 2 else 0)
        pos += skip


process_commands([tk for tk in tokens(str)])
