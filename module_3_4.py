def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word in word or word in root_word:
            same_words.append(word)
    return same_words

result1 = single_root_words("банан", "мандарин", "клубникабанан", "яблбананоко")
result2 = single_root_words("car", "avtocar", "Михаил", "carгонщик")
print(result1)
print(result2)