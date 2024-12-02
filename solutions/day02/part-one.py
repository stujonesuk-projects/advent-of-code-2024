from solutions.day02.common import check_differences, differences

def answer(data):
    data = map(lambda x: x.split(), data)
    data = ((int(x) for x in line) for line in data)
    return sum(map(check_differences, map(differences, data)))
