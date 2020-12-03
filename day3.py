with open('input.txt') as inp:
    m = inp.readlines()
    i, j, t = 0, 0, 1
    for k in [[1, 1], [3, 1], [5,1], [7,1], [1, 2]]:
        tree = 0
        i = 0
        j = 0
        while i < len(m):
            if m[i][j] == '#':
                tree += 1
            i += k[1]
            j = (j + k[0]) % (len(m[0]) - 1)
        t *= tree
    print(t)
