def garland(word):
    degree = 0
    for i in range(1, len(word)):
        if word[:i] == word[-i:]:
            degree = i
    return degree
word=str(input("Enter a word: "))
print(garland(word))