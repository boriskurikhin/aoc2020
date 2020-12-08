'''
    didn't do that well today
    misunderstood part 2, thought we
    had to return the index that caused the loop
    ... 
    spent 40 min debugging why it didn't work
    ehhhhh
'''

with open('input.txt') as ___:
    lines = list(map(lambda x: x.strip(), ___.readlines()))

    def simulate():
        visited = set()
    
        p = acc = last = 0

        while p < len(lines):
            command, val = lines[p].split(' ')
            sign, value = val[0], int(val[1:])

            if p in visited:
                return

            visited.add(p)
            
            if command == 'nop':
                last = p
                p += 1
            elif command == 'acc': 
                acc += -value if sign == '-' else value
                p += 1
            else:
                last = p
                p += -value if sign == '-' else value
        
        print(acc)
    
    for j in range(len(lines)):
        if 'jmp' in lines[j]:
            lines[j] = lines[j].replace('jmp', 'nop')
            simulate()
            lines[j] = lines[j].replace('nop', 'jmp')
        if 'nop' in lines[j]:
            lines[j] = lines[j].replace('nop', 'jmp')
            simulate()
            lines[j] = lines[j].replace('jmp', 'nop')

        