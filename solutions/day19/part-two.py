from itertools import product
from math import ceil

def answer(data):
    def test_combination(test):
        candidate_towels = set(filter(lambda t: t in test, towel_types))
        this_test = {test: 1}
        next_test = {}
        complete = 0
        while this_test:
            for towel in candidate_towels:
                for check in this_test:
                    if check == towel:
                        complete += this_test[check]
                        continue
                    towel_len = len(towel)
                    if towel_len > len(check):
                        continue
                    if check[:towel_len] == towel:
                        if check[towel_len:] not in next_test:
                            next_test[check[towel_len:]] = this_test[check]
                        else:
                            next_test[check[towel_len:]] += this_test[check]
            this_test = next_test
            next_test = {}
        return complete

    towel_types = set(map(lambda x: x.strip(), data[0].split(',')))
    desired_combinations = set(data[2:])
    answer = 0
    while(desired_combinations):
        answer += test_combination(desired_combinations.pop())

    return answer