def answer(data):
    split_data = list(map(lambda x: x.split(), data))
    list1 = sorted(map(lambda x: int(x[0]), split_data))
    list2 = sorted(map(lambda x: int(x[1]), split_data))
    return sum(map(lambda x, y: abs(x-y), list1, list2))
