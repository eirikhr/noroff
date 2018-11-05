def add_underscores(word):
    newWord = "_"
    for i in range(0, len(word)):
        newWord = newWord + word[i] + "_"
    return newWord

phrase = input("What word shall we add underscores to?")
print(add_underscores(phrase))
