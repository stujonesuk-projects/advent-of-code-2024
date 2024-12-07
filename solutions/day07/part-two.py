from solutions.day07.common import tree_combinations, add, mul

def concat(left, right):
    return int(str(left)+str(right))

def answer(data):
    answer = 0
    for line in data:
        total, values = line.split(':')
        total = int(total)
        values = list(map(int, values.strip().split(' ')))
        for operators in tree_combinations([add,mul,concat], len(values)-1, add):
            test = 0
            operators = iter(operators)
            for value in values:
                if test > total or value > total:
                    break
                op = next(operators)
                test = op(test, value)
            if test == total:
                answer += total
                break
    return answer
