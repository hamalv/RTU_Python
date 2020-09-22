num = int(input(f"Ludzu ievadiet eglites augstumu "))
x = 1
for _ in range(num):
    print(" "*num+"*"*x)
    x+=2
    num-=1
    