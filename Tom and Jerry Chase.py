'''
In a classic chase, Tom is running after Jerry as Jerry has eaten Tom's favourite food.
Jerry is running at a speed of X metres per second while Tom is chasing him at a speed of Y metres per second. Determine whether Tom will be able to catch Jerry.
Note that initially Jerry is not at the same position as Tom.
'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(a>b):
        print('NO')
    elif(a==b):
        print('NO')
    else:
        print('YES')
