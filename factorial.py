def fact(n:int)->int:
    if(n<=2): return n
    return n*fact(n-1)
n=int(input("Enter a number: "))
print(f"Factorial of {n} is {fact(n)}")