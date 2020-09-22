def get_char_count(text):
    d = {}
    for i in text:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1   
    return d

def main():
    print(get_char_count("hubba bubba"))
    print(get_char_count(str(3345435342)))
    print(get_char_count("šis ir mans PIRMAIS teikums"))

if __name__ == "__main__":
    main()