def add_mult(num1, num2, num3):
    my_list = [num1, num2, num3]
    my_list = sorted(my_list)
    print(f"Result = ({my_list[0]} + {my_list[1]}) * {my_list[2]} = {(my_list[0]+my_list[1])*my_list[2]}")

def main():
    add_mult(2,9,1)
    add_mult(52,1,2)
    add_mult(5,9,2)

if __name__ == "__main__":
    main()