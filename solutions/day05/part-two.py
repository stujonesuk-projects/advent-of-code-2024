from solutions.day05.common import preprocess, Rule

def answer(data):
    rules, updates = preprocess(data)
    answer = 0
    for update in updates:
        applicable_rules = filter(lambda x: x.before in update and x.after in update, rules)
        counters = dict.fromkeys(update, 0)
        if not all(list(map(lambda x: x.check(update, counters), applicable_rules))):
            answer += [x for x,y in counters.items() if y == 0][0]
    return answer
