from collections import Counter

def answer(data):
    split_data = list(map(lambda x: x.split(), data))
    list1 = map(lambda x: int(x[0]), split_data)
    list2 = Counter(map(lambda x: int(x[1]), split_data))
    return sum(map(lambda x: x * list2[x], list1))
