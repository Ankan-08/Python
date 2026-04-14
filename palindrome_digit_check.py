n:int=int(input("Enter a number: "))
m:int=n
sum:int=0
while(m>0):
    sum=sum*10+(m%10)
    m//=10
if(sum==n):
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")
