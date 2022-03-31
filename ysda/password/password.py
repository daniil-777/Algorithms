def password_strength(password: str) -> str:
    password_low = password.lower()
    if len(password) < 8 or (password_low.count('anna') >= 1) \
            or unique(password) < 4:
        return 'weak'
    else:
        if any(c.islower() for c in password) and any(c.isupper() for c in password)\
                and any(c.isdigit() for c in password):
            return 'strong'
        else:
            return 'weak'


def unique(password: str) -> int:
    dict1 = set()
    count = 0
    for char in password:
        if char not in dict1:
            dict1.add(char)
            count += 1
    return count
