#prefix sums, etc
with open('input.txt') as ___:
    lines = list(map(lambda x: int(x.strip()), ___.readlines()))
    from collections import deque
    prefix, cache = [], deque()
    N, L = 25, 0
    
    for i in range(N):
        cache.append(lines[i])
        prefix.append(lines[i] + prefix[-1] if len(prefix) > 0 else lines[i])
        L += 1
    
    for i in range(L, len(lines)):
        good = False
        
        for store in cache:
            if lines[i] - store in cache:
                good = True
                break
        
        if not good:
            print('1:', lines[i])
            for l in range(0, i):
                sm = la = lines[l]
                for r in range(l + 1, i):
                    sm = min(sm, lines[r])
                    la = max(la, lines[r])
                    if prefix[r] - prefix[l] + lines[l] == lines[i]:
                        print('2:', sm + la)
                        exit()
        
        cache.popleft()
        cache.append(lines[i])
        prefix.append(lines[i] + prefix[-1])
            
                