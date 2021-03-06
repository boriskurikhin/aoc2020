
# graph searches, bfs & dfs
with open('input.txt') as inp:
    lines = inp.readlines()
    answer1 = 0
    contains = {}
    for line in lines:
        line = line.strip().split('contain')
        bagName = line[0].strip()[:line[0].index(' bag')]
        contains[bagName] = []
        for b in line[1].strip().split(','):
            b = b.strip()
            # nothing to see here
            if b.startswith('no'): continue
            quantity = int(b[0:b.index(' ') + 1])
            mapsTo = b[b.index(' ') + 1:b.index(' bag')]

            contains[bagName].append((quantity, mapsTo))

    # dfs
    def dfs(b, map):
        _, bag = b
        ans = 1

        for pair in map[bag]:
            q, bn = pair
            ans += q * dfs(pair, map)

        return ans


    def bfs(b, map):
        from collections import deque
        
        q = deque()
        q.append(b)
        
        while len(q):
            quantity, bag = q.popleft()
            if 'shiny gold' in bag and quantity > 0:
                return True
            for bags in map[bag]:
                q.append(bags)
        return False

    # run bfs on all bags
    for k in contains.keys():
        if bfs((1, k), contains):
            answer1 += 1

    # run the dfs from shiny gold
    print(answer1 - 1, dfs((1, 'shiny gold'), contains) - 1)