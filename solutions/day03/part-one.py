from re import findall

def answer(data):
    data = '\n'.join(data)
    matches = findall('mul\\([0-9]{1,3},[0-9]{1,3}\\)', data)
    return sum(map(lambda x: x[0] * x[1], map(lambda x: [int(x) for x in x[4:-1].split(',')], matches)))
 