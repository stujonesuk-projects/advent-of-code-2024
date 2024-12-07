tree_cache = {}

def tree_combinations(options, depth, prefix = None):
    this_hash = hash(str(options)+str(depth)+str(prefix))
    deeper_hash = hash(str(options)+str(depth-1)+str(prefix))
    if this_hash not in tree_cache:
        if depth == 1:
            if prefix is None:
                tree_cache[this_hash] = options
            else:
                tree_cache[this_hash] = list(map(lambda a: [prefix, a], options))
        else:
            if deeper_hash not in tree_cache:
                tree_combinations(options, depth - 1, prefix)
            tree_cache[this_hash] = [[*l,r] for l in tree_cache[deeper_hash] for r in options]
    return tree_cache[this_hash]

def mul(left, right):
    if left is None:
        return right
    return left * right

def add(left, right):
    if left is None:
        return right
    return left + right
