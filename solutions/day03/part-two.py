from re import findall

def do_dont_tracker(values):
    do = True
    values = iter(values)
    while((i := next(values, None)) is not None):
        if i[0:4] == 'mul(':
            if do:
                mul_args = i[4:-1].split(',')
                yield int(mul_args[0]) * int(mul_args[1])
            else:
                continue
        elif i[0:6] == 'don\'t(':
            do = False
            continue
        elif i[0:3] == 'do(':
            do = True
            continue

def answer(data):
    data = '\n'.join(data)
    matches = findall('(mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don\'t\\(\\))', data)
    return sum(do_dont_tracker(matches))
 