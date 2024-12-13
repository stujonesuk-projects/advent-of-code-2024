from itertools import batched, chain
from solutions.day13.common import Problem, getcontext

getcontext().prec = 5

def answer(data):
    problem = lambda x: Problem(x)
    return sum(map(lambda x: x.cost, map(problem, batched(chain(data,['']), 4))))
