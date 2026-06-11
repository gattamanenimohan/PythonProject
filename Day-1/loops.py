# print(list(range(0,10)))

# even numbers
i=1
while i<=10:
    if(i%2==0):
        print(i)
    i=i+1


# odd numbers
i=1
while i<=10:
    print(i)
    i=i+2


# from 0-10
i=1
while i<=10:
    print(i)
    i=i+1

# even numbers
i=2
while i<=10:
    print(i)
    i=i+2

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
# Take input from user
num = int(input("Enter the number of terms: "))
fibonacci(num)