from collections import defaultdict

def blink(data, blink_count):
    stones = defaultdict(lambda: 0)
    for stone in map(int,data[0].split(' ')):
        stones[stone] += 1
    blink = 0
    while blink < blink_count:
        blink += 1
        old_stones = stones
        stones = defaultdict(lambda: 0)
        for k,v in old_stones.items():
            ks = str(k)
            if k == 0:
                stones[1] += v
            elif len(ks) % 2 == 0:
                stones[int(ks[:len(ks) // 2])] += v
                stones[int(ks[len(ks) // 2:])] += v
            else:
                stones[k * 2024] += v
    return sum(stones.values())
