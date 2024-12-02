from solutions.day02.common import check_differences, differences
from itertools import combinations, chain

def check_differences_any(sets_of_values):
    for i in sets_of_values:
        if check_differences(differences(i)):
            return 1
    return 0    

def answer(data):
    data = map(lambda x: x.split(), data)
    data = ([int(x) for x in line] for line in data)
    data = (chain(combinations(line, len(line)), combinations(line, len(line)-1)) for line in data)
    return sum(map(check_differences_any, data))
