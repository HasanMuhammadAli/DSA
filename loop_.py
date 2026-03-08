'''
#Factorial Calculation
factorail = 1
num = int(input("Enter number to find factorial: "))
for i in range (1, num+1):
    factorail *= i
print(factorail)

#Arithmetic Series Summation
sum = 0
num = int(input("Enter the number: "))
for i in range(num+1):
    sum += i
print(sum)

sum_way2 = (num * (num+1))/2
print(sum_way2)


#Power Function 


def power(x, n):
    result = 1
    for i in range(abs(n)):
        result *= x
    if (n < 0) and (n%2 != 0):
        result *= (-1)
    return result

x = int(input("Enter base: "))
n = int(input("Enter exponent: "))
ans = power(x, n)
print("Power of "+ str(x) +" raise to "+ str(n) +" = "+ str(ans))


#Fibonacci Sequence Generation
def fibonacci(n):
    second_to_last, last = 0, 1
    sequence = [0, 1]
    for i in range(2, n):
        next = last + second_to_last
        sequence.append(next)
        second_to_last = last
        last = next
    return sequence

num = int(input("Enter how many numbers to be in fibonacci sequence: "))
ans = fibonacci(num)
print("Fibonacci : ")
print(ans)



#Vector Dot Product
def dotProduct(A, B):
    ans = 0
    if len(A) == len(B):
        for i in range(len(A)):
            ans += (A[i] * B[i])
        return ans
    else:
        print("Length of vectors not same.")
A=[0, 1, 2]
B=[2, 3, 4]
print(dotProduct(A, B))

'''

#Numerical Integration (Left Riemann Sum)
def numIntegral(a, b, n, fn):
    delta_x = (b - a) / n
    area = 0
    x = a
    for _ in range(n):
        area += fn(x) * delta_x
        x += delta_x
    return area

fn = lambda x: x*x
print(numIntegral(10, 100, 150, fn))
