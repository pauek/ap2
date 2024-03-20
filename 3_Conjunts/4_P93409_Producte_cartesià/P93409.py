
def cartesian_product(a: set[int], b: set[int]) -> set[tuple[int, int]]:
    return set((i, j) for i in a for j in b)