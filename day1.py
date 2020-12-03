# simple 3 sum
with open('input.txt') as inp:
    k = sorted(list(map(lambda x: int(x), inp.readlines())))
    l = 0
    while l < len(k):
        m = l + 1
        r = len(k) - 1
        while m < r:
            s = sum([k[l], k[m], k[r]])
            if s == 2020:
                print(' =', k[l] * k[m] * k[r])
                break
            elif s < 2020:
                m += 1
            else:
                r -= 1
        l += 1