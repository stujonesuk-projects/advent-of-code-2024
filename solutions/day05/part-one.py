from solutions.day05.common import preprocess, Rule

def answer(data):
    rules, updates = preprocess(data)
    answer = 0
    for update in updates:
        applicable_rules = filter(lambda x: x.before in update and x.after in update, rules)
        if all(map(lambda x: x.check(update), applicable_rules)):
            answer += update[(len(update) - 1) // 2]
    return answer
