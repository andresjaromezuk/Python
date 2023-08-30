# def is_palindrome(string):
#     backwards = string[::-1]
#     return backwards.casefold() == string.casefold()


# word = input("Introduce una palabra:")
# if is_palindrome(word):
#     print(f"{word} es palindrome")
# else:
#     print(f"{word} no es palindrome")


def palindrome_sentence(sentence):
    list = ""
    for l, v in enumerate(sentence):
        if v.isalnum():
            list += v
    reverso = list[::-1]
    return list.casefold() == reverso.casefold()

oracion = palindrome_sentence("Neuquen ese neuquen")

print(oracion)