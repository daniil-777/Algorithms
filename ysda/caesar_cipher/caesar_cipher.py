def caesar_encrypt(message: str, n: int) -> str:
    result = ""
    finalletter = 'a'
    for ch in message:
        if ch.isalpha():
            print(ord(ch))
            number = ord(ch) + n
            print(number)
            if ch.isupper():
                if number > ord('Z'):
                    number -= 26
                elif number < ord('A'):
                    number += 26
                finalletter = chr(number)
            elif ch.islower():
                if number > ord('z'):
                    number -= 26
                elif number < ord('a'):
                    number += 26
                finalletter = chr(number)
            result += finalletter
        else:
            result += ch
    return result
