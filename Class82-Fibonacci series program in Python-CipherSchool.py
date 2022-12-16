def fibonacci_seq(n):
    a = 0 # first number, a = 1
    b = 1 # second number, b = 1
    if n == 1 :
        print(a)

    elif n == 2:
        print(a, b) #ab, 01

    else:
        print(a,b ,end =" ")
        for i in range(n-2):
            c = a + b # c = 1, 2, 3
            a = b # a = 1, 1 2
            b = c # b = 1 2, 3
            print(b, end=" ")
n=int(input())
fibonacci_seq(n)
