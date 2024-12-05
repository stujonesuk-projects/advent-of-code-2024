def preprocess(data):
    data = '\n'.join(data)
    data = data.split('\n\n')
    rules = list(map(Rule, data[0].split('\n')))
    updates = map(lambda x: list(map(int, x.split(','))), data[1].split('\n'))
    return rules, updates

class Rule:
    def __init__(self, rule):
        rule = map(int,rule.split('|'))
        self.before = next(rule)
        self.after = next(rule)

    def check(self, values, counters = None):
        if counters:
            counters[self.before] -= 1
            counters[self.after] += 1

        return values.index(self.before) < values.index(self.after)

