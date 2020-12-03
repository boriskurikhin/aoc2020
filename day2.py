# xor thing
with open('input.txt') as inp:
    ans = 0
    for line in inp.readlines():
        tokens = line.split()
        a, b = (map(lambda x: int(x), tokens[0].split('-')))
        find = tokens[1][0]
        search = tokens[2]
        if (search[a-1] == find) ^ (search[b-1] == find):
            ans += 1
    print(ans)

