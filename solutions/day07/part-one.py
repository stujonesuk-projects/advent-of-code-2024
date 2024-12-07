from solutions.day07.common import tree_combinations, add, mul

def answer(data):
    answer = 0
    for line in data:
        total, values = line.split(':')
        values = list(map(int, values.strip().split(' ')))
        for operators in tree_combinations([add,mul], len(values)-1, add):
            test = 0
            operators = iter(operators)
            for value in values:
                test = next(operators)(test, value)
            if test == int(total):
                answer += int(total)
                break
    return answer
