'''
Bob received an assignment from his school: he has two numbers A and B, and he has to find the sum of these two numbers.
Alice, being a good friend of Bob, told him that the answer to this question is C.Bob doesn't completely trust Alice and asked you to tell him if the answer given by Alice is correct or not.
If the answer is correct print "YES", otherwise print "NO" (without quotes).
'''
n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if (a+b)==c:
        print('YES')
    else:
        print('NO')
