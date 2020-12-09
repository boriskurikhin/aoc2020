#prefix sums, etc
with open('input.txt') as ___:
    lines = list(map(lambda x: int(x.strip()), ___.readlines()))
    from collections import deque
    pre, prefix, cache = [], [lines[0]], deque()
    N, L = 25, 0
    
    for i in range(N):
        pre.append(lines[i])
        cache.append(lines[i])
        prefix.append(lines[i] + prefix[-1])
        L += 1
    
    for i in range(L, len(lines)):
        good = False
        
        for store in cache:
            if lines[i] - store in cache:
                good = True
                break
        
        L += 1
        cache.popleft()
        cache.append(lines[i])

        if not good:
            print('1: ', lines[i])
            for left in range(0, L):
                mini, maxi = lines[left], lines[left]
                for right in range(left + 1, L):
                    mini = min(mini, lines[right])
                    maxi = max(maxi, lines[right])

                    if prefix[right] - prefix[left] + lines[right] == lines[i]:
                        print('2: ', mini + maxi)
                        exit(0)
                        
        pre.append(lines[i])
        prefix.append(lines[i] + prefix[-1])
            
                