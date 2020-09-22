i = 0
r = 100
while i < r:
    i += 1
    if i%5==0 and i%7==0:
        print("FizzBuzz")
        continue
    elif i%5==0:
        print("Fizz")
        continue
    elif i%7==0:
        print("Buzz")
        continue
    print(i)
    