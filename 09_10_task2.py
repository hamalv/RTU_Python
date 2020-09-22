d = {'a':3, 'b':6, 'c':2, 'd':32, 'e':21, 'f':2}

def replace_dict_value(d, bad_value, good_value):
    for key,value in d.items():
        if value == bad_value:
            d[key] = good_value
    return d

def main():
    print(replace_dict_value(d, 2, 7))

if __name__ == "__main__":
    main()