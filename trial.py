ex1
def create_triangle(height, symbol='#'):
    triangle = []
    for i in range(height):
        row = [symbol] * (i + 1)
        triangle.append(row)
    return triangle
print(create_triangle(3))


ex2

def func(a,b):
    if a < b :
        for i in range(a , 0 , -1):
            if a % i == 0 and b % i == 0:
                return i
    elif b < a :
        for j in range(b , 0 , -1):
            if b % i == 0 and a % i == 0 :
                return i 
    else:
        return 1
print(func(int(input('Enter the number1: ')),int(input('Enter the number2: '))))


ex3
count = 0
def fib(n):
    global count
    count += 1
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(int(input('Enter the num: '))))
print(count)


ex4
def prime_factors(n):
    listt = []
    for i in range(2, n + 1):
        if n % i == 0:
            count = 0
            for x in range(1, i):
                if i % x == 0:
                    count += 1
            if count < 2:
                listt.append(i)
    return list(set(listt))

print(prime_factors(100))

ex5
def jumping_frog(p,h):
    s=True
    for i in range(len(p)-1):
        if abs(p[i+1]-p[i])<=h:
            s=True
        else:
            s=False
            print('Game over')
            return
    print('Frog wins')
jumping_frog([1,3],2)
jumping_frog([4,5,2],2)