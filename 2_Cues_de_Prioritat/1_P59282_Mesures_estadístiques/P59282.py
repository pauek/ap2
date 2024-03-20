from yogi import *
from heapq import *

Heap = list[int]

heap = Heap()
sum, mx = 0, 0

for cmd in tokens(str):
    if cmd == "number":
        n = read(int)
        sum += n
        mx = max(mx, n) if heap else n
        heappush(heap, n)
    elif cmd == "delete" and heap:
        sum -= heappop(heap)

    if not heap:
        print("no elements")
    else:
        print(f"minimum: {heap[0]}, maximum: {mx}, average: {sum / len(heap):.4f}")
