#prefix sums, etc
with open('input.txt') as ___:
    lines = list(map(lambda x: int(x.strip()), ___.readlines()))
    from collections import deque
    prefix, cache = [lines[0]], deque()
    N, L = 25, 0
    
    for i in range(N):
        cache.append(lines[i])
        prefix.append(lines[i] + prefix[-1])
        L += 1
    
    for i in range(L, len(lines)):
        good = False
        
        for store in cache:
            if lines[i] - store in cache:
                good = True
                break
        
        if not good:
            print('1: ', lines[i])
            for left in range(1, i):
                mini, maxi = lines[left], lines[left]
                for right in range(left + 1, i):
                    mini = min(mini, lines[right])
                    maxi = max(maxi, lines[right])
                    if prefix[right] - prefix[left] == lines[i]:
                        print('2: ', mini + maxi)
                        exit(0)
        
        cache.popleft()
        cache.append(lines[i])
        prefix.append(lines[i] + prefix[-1])
            
                