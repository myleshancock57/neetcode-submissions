def get_longer_word(word1: str, word2: str) -> str:
    i = len(word1)
    j = len(word2)
    if (i > j):
        return word1
    elif i == j:
        return word1
    else:
        return word2



# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
