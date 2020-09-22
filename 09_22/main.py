import math

# My lib
import randomGen as r

r_num1 = []
r_num2 = []

def main():
    r.RandomGen(r_num1)
    r.RandomGen(r_num2)
    print(r_num1)
    print(r_num2)
    print(math.prod(r_num1))
    print(math.prod(r_num2))
    r.sum_prod(r_num1, r_num2)

if __name__ == "__main__":
    main()