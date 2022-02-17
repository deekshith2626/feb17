evensum = oddsum = 0
n=int(input())
for i in range(1,n+1):
    if(i%2==0):
        evensum+=i
       
    else:
        oddsum+=i



print("sum of even numbers",evensum)
print("sum of odd numbers",oddsum)
        
