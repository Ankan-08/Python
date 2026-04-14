n:int=int(input("Enter a number: "))
l=len(str(n))
m=n
sum:int=0
while(m>0):
  r=m%10
  sum+=pow(r,l)
  m//=10
if(sum==n):
  print(f"{n} is an Armstrong number")
else:
  print(f"{n} is not an Armstrong number")
  
