def factorial(n):
    val=1
    for i in range(1,n+1):
        val=val*i
    return val


n=int(input("Enter a number to find its factorial"))
print(factorial(n))