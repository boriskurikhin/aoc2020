'''
    4d game of life...
'''
with open('input.txt') as ___:
    lines =  ___.readlines()
    cubes = set()
    for r,l in enumerate(lines):
        l = l.strip()
        for c, m in enumerate(l):
            if m == '#':
                cubes.add((c, r, 0, 0))

    def calc_hood(cube):
        ans = []
        for x in [cube[0] - 1, cube[0], cube[0] + 1]:
            for y in [cube[1] - 1, cube[1], cube[1] + 1]:
                for z in [cube[2] - 1, cube[2], cube[2] + 1]:
                    for w in [cube[3] - 1, cube[3], cube[3] + 1]: 
                        newCube = (x,y,z,w)
                        if newCube == cube: continue
                        ans.append(newCube)
        return ans
    
    for cycle in range(6):
        state = set()

        for curCube in cubes:
            hood = calc_hood(curCube)
            alive = set()
            dead = set()
            for checkCube in hood:
                if checkCube in cubes:
                    alive.add(checkCube)
                else: dead.add(checkCube)
            if len(alive) in [2,3]:
                state.add(curCube)

            for deadCube in dead:
                others = calc_hood(deadCube)
                potential = set()
                for checkCube in others:
                    if checkCube in cubes:
                        potential.add(checkCube)
                if len(potential) == 3:
                    state.add(deadCube)
        from copy import deepcopy
        cubes = deepcopy(state)
    print(len(cubes))
