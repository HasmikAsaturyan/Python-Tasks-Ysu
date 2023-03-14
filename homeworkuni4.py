1
s = 0
for i in range(3):
    x = int(input('Enter the number: '))
    s += x
print(s)

2
b1 = int(input('Enter the number: '))
q = int(input('Enter the number: '))
n = int(input('Enter the number: '))
bn = b1 * q**(n-1)
print(bn)

3
n = int(input('Enter the number: '))
if n % 2 == 0:
    print(f'the number {n} is even')
else:
    print(f'the number {n} is odd')

4
mylist = [1,2,3,4,5]
for i in range(len(mylist)-1):
    if mylist[i+1] - mylist[i] == 1:
        print('arithmetic progression')
    else:
        print('no pattern found')

5
x = int(input('Enter the number: '))
if len(str(x)) == 3:
    print('no')
elif x % 3 == 0 and x % 23 == 0:
    print('yes')
else:
    print('no')

6
a = int(input('Enter the number: '))
b = int(input('Enter the number: '))
c = int(input('Enter the number: '))
if b**2 - 4*a*c == 0:
    x = -b/(2*a)
    print(x)
elif b**2 - 4*a*c < 0:
    print('no solution')
else:
    print(f'x1 = {-b + ((b**2 - 4*a*c)**0.5)/(2*a)} x2 = {-b - ((b**2 - 4*a*c)**0.5)/(2*a)}  ')
    

8
n = int(input('Enter the number: '))
for i in range(1,11):
    print(f'{n} * {i} = {n * i}')

9
mylist = []
n = int(input('Enter: '))
for i in range(0,n):
    x = int(input('Enter: '))
    mylist.append(x)
print(mylist)

10
n = int(input('Enter: '))
for i in range(1,n+1):
    if n % i == 0:
        print(i)

11
count = 0
newlist = []
n = int(input('Enter: '))
for i in range(n):
    x = int(input('enter views: '))
    newlist.append(x)
for i in range(len(newlist)-1):
    if newlist[i + 1] > newlist[i]:
        count += 1
print(count)


12
listt = []
n = int(input('Enter: '))
for i in range(n):
    text = input('Enter the text: ')
    listt.append(text)
print(listt[::-1])

13
n = int(input('Enter: '))
k = 1
for i in range(1,n+1):
    k *= i
print(k)

14
n = int(input('Enter: '))
for i in range(1,n):
    if i**2 < n:
        print(i**2)
    else:
        continue

15
n = int(input('Enter: '))
for i in range(1,n+1):
    if 2**i < n:
        print(2**i)

16
def poweroftwo(n):
    if n == 1:
        return True
    elif n % 2 != 0 or n == 0:
        return False
    return poweroftwo(n/2)
print(poweroftwo(8))

17
s = ''
while True:
    text = input('Enter the text: ')
    if text == 'stop':
        print(s[0:-1])
        break
    else:
        s += text 
print(s)

18
s = 0
mylist = [-1,-2,-3,-4,-5,7,-3]
for i in mylist:
    if i >= 0:
        print(s)
        break
    else:
        s+=i

19
n = int(input('Enter the number: '))
print(str(n*2)[::-1])

20
newlist = []
n = input('Enter the number: ')
for i in n:
    newlist.append(int(i))
for i in range(len(newlist)-1):
    if newlist[i+1] - newlist[i] == 1:
        print('true')
    else:
        print('false')
