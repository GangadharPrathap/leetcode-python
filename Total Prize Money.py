'''
In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:
Top 10 participants receive rupees X each.
Participants with rank 11 to 100 (both inclusive) receive rupees Y each.
Find the total prize money over all the contestants.'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    d=10*a+90*b
    print(d)
