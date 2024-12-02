def differences(values):
    i = iter(values)
    prev = next(i, None)
    if prev is None:
        return
    while((curr := next(i, None)) != None):
        yield curr - prev
        prev = curr

def check_differences(differences):
    direction = None
    for difference in differences:
        if difference == 0:
            return 0
        if abs(difference) > 3:
            return 0
        if not direction:
            direction = difference / abs(difference)
        if direction != difference / abs(difference):
            return 0
    return 1
