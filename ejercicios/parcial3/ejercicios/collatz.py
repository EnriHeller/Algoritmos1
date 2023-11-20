def collatz(n):
    print(n)

    if n<=1:
        return 
    
    if n % 2 == 0:
        nuevo_n = n//2
        collatz(nuevo_n)
    else:
        nuevo_n = (n*3) + 1
        collatz(nuevo_n)

collatz(0.5)