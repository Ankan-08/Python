def fact(n:int)->int:
    if(n<=2): return n
    return n*fact(n-1)
flag : bool=True
while(flag):
    try:
        n : int=int(input("Enter a number: "))
        print(f"Factorial of {n} is {fact(n)}")
        flag=False
    except Exception as e:
        print("Only Numbers are allowed")