def caesar_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():                        # буква ли это
            shift_char = ord(char) + 3
            if char.isupper():                    # большая ли это буква
                result += chr(shift_char) if shift_char <= ord("Z") else chr(shift_char - 26)
            else:
                result += chr(shift_char) if shift_char <= ord("z") else chr(shift_char - 26)
        else:
            result += char
    return result

text = input("Введите фразу: ")
encrypted_text = caesar_cipher(text)
print("Зашифрованный текст: ", encrypted_text)


