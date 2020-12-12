
'''
    https://www.khanacademy.org/math/geometry/hs-geo-transformations/hs-geo-rotations/a/rotating-shapes

    basically...
'''
with open('input.txt') as ___:
    lines = list(map(lambda x: x.strip(), ___.readlines()))
    y, x = 0, 0
    wy,wx = 1, 10

    for line in lines:
        d = line[0]
        k = int(line[1:])

        if d == 'F':
            x += k * wx
            y += k * wy
        elif d == 'L':
            for j in range(k // 90):
                wx, wy = -wy, wx
        elif d == 'R':
            for j in range(k // 90):
                wx, wy = wy, -wx
        elif d == 'N':
            wy += k
        elif d == 'S':
            wy -= k
        elif d == 'E':
            wx += k
        elif d == 'W':
            wx -= k
    print(abs(x) + abs(y))
            
            
        