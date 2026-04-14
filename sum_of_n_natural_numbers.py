flag :bool =True
while(flag):
    try:
        n : int =int(input("Enter a number: "))
        sum : int =0
        for i in range(1,n+1):
            sum+=i
        print(f"Sum of {n} natural number: {sum}")
        flag=False
    except Exception as e:
        print("only numbers are allowed")
