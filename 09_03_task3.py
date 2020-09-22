sentence = input("Ievadiet teikumu: ")
sentence_array = sentence.split()
sentence_len = len(sentence_array)
new_sentence = []
i = 0
while i < sentence_len:
    new_word = sentence_array[i]
    new_word = new_word[::-1]
    new_sentence.append(new_word)
    i += 1
new_sentence = " ".join(new_sentence)
print(new_sentence)