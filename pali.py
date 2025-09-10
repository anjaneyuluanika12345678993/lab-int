n=int(input("n"))
count=0
x=n
while x>0:
    r=x%10
    count=count*10+r
    x=x//10
print(count==n)