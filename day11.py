#!/usr/bin/env Python3
# time to get that shebang out

# game of life sort of thing
# i hate python for .copy being shallow

from collections import deque
import copy
with open('input.txt') as ___:
    lines = list(map(lambda x: list(x.strip()), ___.readlines()))
    change = True
    dirs = [(1,0), (-1,0), (0, 1), (0, -1), (1,1), (-1, 1), (1, -1), (-1, -1)]
    count = 0
    
    q = deque()
    q.append(lines)

    # part 2 search
    def dfs(r, c, yd, xd, Y, X, grid):
        if r < 0 or c < 0 or r >= Y or c >= X:
            return True
        if grid[r][c] == 'L':
            return True
        if grid[r][c] == '#':
            return False 
        return dfs(r + yd, c + xd, yd, xd, Y, X, grid)

    while change:
        top = q.popleft()
        modify = copy.deepcopy(top)
        change = False
        for r in range(len(top)):
            for c in range(len(top[0])):
                v = top[r][c]
                occ = 0
                for k in dirs:
                    y, x = k
                    if not dfs(r + y, c + x, y, x, len(top), len(top[r]), top):
                        occ += 1
                # print(r,c,occ,count)
                if v == 'L' and occ == 0:
                    modify[r][c] = '#'
                    change = True
                if v == '#' and occ >= 5:
                    modify[r][c] = 'L'
                    change = True
        if not change:
            occ = 0
            for r in modify:
                occ += r.count('#')
            print('answer', occ)
            exit(0)
        q.append(modify)
        count += 1