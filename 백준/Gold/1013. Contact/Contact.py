import re
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(input().strip())
    
    if m:
        print('YES')
    else:
        print('NO')