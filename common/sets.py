from functools import reduce

def consolidate(sets):
    newsets = sets
    oldsets = None
    while newsets != oldsets:
        oldsets = newsets
        newsets = set(map(lambda y: reduce(lambda a,b: a.union(b) if not a.isdisjoint(b) else a, y[1], y[0]),map(lambda x: (x, oldsets - {x}), oldsets)))
    return newsets
