def fib(x):
    if x <= 1:
        return x
    else:
        return (fib(x-1) + fib(x-2))


n = int(input("Enter number of terms: "))
print("Fibonacci sequence:")

for i in range(n):
    print(fib(i))

