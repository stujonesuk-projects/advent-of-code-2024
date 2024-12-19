from itertools import product
from math import ceil

def answer(data):
    def test_combination(test):
        candidate_towels = set(filter(lambda t: t in test, towel_types))
        this_test = set([test])
        next_test = set()
        while len(this_test) > 0:
            for towel in candidate_towels:
                for check in this_test:
                    if check == towel:
                        possible_combinations.add(test)
                        return
                    towel_len = len(towel)
                    if towel_len > len(check):
                        continue
                    if check[:towel_len] == towel:
                        next_test.add(check[towel_len:])
            this_test = next_test
            next_test = set()

    towel_types = set(map(lambda x: x.strip(), data[0].split(',')))
    desired_combinations = set(data[2:])
    possible_combinations = set()
    while(desired_combinations):
        test_combination(desired_combinations.pop())

    return len(possible_combinations)