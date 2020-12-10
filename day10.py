# dynamic programming, took me for ever and had to research on the internets
# but we finally got it..
with open('input.txt') as ___:
    lines = [0] + sorted(list(map(lambda x: int(x.strip()), ___.readlines())))
    
    from collections import deque
    def bfs(inp, s):
        q = deque()
        q.append(s)
        seen = set()

        paths = [0] * len(inp)
        paths[0] = 1

        while len(q):
            top = q.popleft()
            for node in inp:
                if node - top <= 3 and node - top >= 1:
                    paths[inp.index(node)] += paths[inp.index(top)]
                    if node not in seen:
                        q.append(node)
                        seen.add(node)
        return paths[-1]
    print(bfs(lines, 0))

