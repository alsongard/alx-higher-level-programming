def uppercase(str):
    for letter in str:
        unicode_char = ord(letter)
        result = unicode_char - 32
        print(chr(result), end="")
