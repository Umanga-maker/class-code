def Fibonacci(n):

    #Base case
    if n <= 1:
        return n
    
    #Previous Fibonacci numbers
    one_back = Fibonacci(n - 1)
    two_back = Fibonacci(n - 2)

    #Result
    return one_back + two_back

#Main program
# n = int(input('Enter n: '))
# result = Fibonacci(n)
# print('Fib(n) =', result)

for x in range(17):
    print(Fibonacci(x))
