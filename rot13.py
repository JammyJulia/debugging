
# Mērķis: 
# šifrēt tekstu ROT13 kodējumā


def rot13(texts):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = alphabet.index(char)
            if is_upper:
                new_index = (char_index + 13) % 26
                print(new_index)
            else:
                new_index = (char_index + 13) % 26 + 26
            result += alphabet[new_index] 
        else:
            result += char        

    return result

print("Enter a text to ROT13 encode")
text = input()
encrypted_text = rot13(text)
print("ROT13 Encoded Text:", encrypted_text)

# Kādas kļūdas izdevies atrast?
# missing spaces when inside 'if'
# evem MORE missing spaces
# misspelled 'alphabet'
# misspelled 'rot13'
# 'if char.isalpha() else char' dont even know whats its supposed to be, deleting it
# 
#
