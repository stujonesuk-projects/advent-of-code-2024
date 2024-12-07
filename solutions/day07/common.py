def tree_combinations(options, depth, prefix = None):
    if depth == 1:
        for a in options:
            if prefix is None:
                yield [a]
            else:
                yield [prefix, a]
    else:
        for a in options:
            for b in tree_combinations(options, depth - 1, prefix):
                yield *b, a

def mul(left, right):
    if left is None:
        return right
    return left * right

def add(left, right):
    if left is None:
        return right
    return left + right
