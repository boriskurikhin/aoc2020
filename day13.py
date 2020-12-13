'''
    math. shoutout larry nyc.
    i can't take credit entirely for part 2
'''
with open('input.txt') as ___:
    lines = list(map(lambda x: x.strip(), ___.readlines()))
    times = list(map(lambda x: int(x) if x != 'x' else 'x', lines[1].split(',')))
    
    t = []
    for i, ti in enumerate(times):
        if ti == 'x': continue
        t.append((i, ti, 0))

    while len(t) > 1:
        bus1 = t[0][1]
        bus2 = t[1][1]
        offset = t[1][0]
        time = t[0][2]

        print(t)
        while True:
            # 7 + 1 % 13 == 0
            # solving this one pair at a time
            # greedy brute force
            if (time + offset) % bus2 == 0:
                break 
            time += bus1
        
        t = [(0, bus1 * bus2, time)] + t[2:]
    print(t[0][2])