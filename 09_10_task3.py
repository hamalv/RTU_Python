aa = {'a':3, 'b':6, 'c':2, 'd':32, 'e':21, 'f':2}

ab = {'a':3, 'b':6, 'c':2, 'd':32, 'e':21, 'f':2}
ab_list = (2,3,4,5,6)

def clean_dict_value(d, bad_val):
    new_d = {}
    for key,value in d.items():
        if value != bad_val:
            new_d[key] = value
    return new_d

def clean_dict_value_ab(d, bad_val):
    new_d = {}
    for key,value in d.items():
        if value not in bad_val:
            new_d[key] = value
    return new_d

def main():
    print(clean_dict_value(aa, 3))
    print(clean_dict_value_ab(ab, ab_list))

if __name__ == "__main__":
    main()