# binary search type of thing
with open('input.txt') as inp:
    # kind of just looked at all seats, found upper & lower bound
    # and went from there...
    seats = set([_ for _ in range(63, 936)])
    lines = inp.readlines()
    a = [[False] * 8] * 128
    total = -1
    for line in lines:
        line = line.strip()
        l,r = 0, 128
        for c in line[0:7]:
            if c == 'F': r -= (r - l) // 2
            else: l += (r - l) // 2
        ans = l * 8
        l,r = 0, 8
        for c in line[7:]:
            if c == 'L': r -= (r - l) // 2
            elif c == 'R': l += (r - l) // 2
        ans += l
        seats.remove(ans)
        total = max(total, ans)
    print('highest', total)
    print('my seat', list(seats)[0])