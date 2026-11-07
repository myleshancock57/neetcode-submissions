def remove_fourth_character(word: str) -> str:
    i = word[:3]
    j = word[4:]
    new_word =  i + j
    return new_word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
