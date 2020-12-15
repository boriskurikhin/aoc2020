# not sure what optimization i was to do here
# but we got 343rd rank by brute force lol
with open('input.txt') as ___:
    lines = list(map(lambda x: int(x), ___.read().split(",")))
    store, time = {}, 0
    for i, j in enumerate(lines):
        store[j] = i + 1
        time += 1 
    last = lines[-1]
    while time != 2020:
        if last in store:
            timeDiff = time - store[last]
            store[last] = time
            last = timeDiff
        else:
            store[last] = time
            last = 0
        time +=1
    print(last)