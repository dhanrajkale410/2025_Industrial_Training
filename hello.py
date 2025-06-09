def facto(n) :
    if(n==0 or n==1) :
        return (1)
    else : 
        return (n*facto(n-1))
num = int(input("Enter a Number : "))
print(f"Factorial of {num} = {facto(num)}")