sentence = []
rev_sentence = []

def is_palindrome(text):
    sentence = (" ".join([word for word in text.split()]))
    rev_sentence = (" ".join([word[::-1] for word in text.split()[::-1]]))
    return sentence == rev_sentence

def main():
    print(is_palindrome("alus sula"))

if __name__ == "__main__":
    main()