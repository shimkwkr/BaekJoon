def power(a,b,c):
    if b == 1:
        return a%c
    
    if b%2==0:
        new_a = power(a, b/2, c)
        return (new_a * new_a)%c
    else :
        new_a = power(a, (b-1)/2, c)
        return (new_a * new_a * a)%c

a,b,c = map(int, input().split())

print(power(a,b,c))