import random
import string

def password_generator(min_length, numbers=True, special_characters=True):
    """Generate a string password with length between min_length and min_length +10
        If numbers than password will contain at least one digit
        If special_characters than password will contain at least one puctuation character"""

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    chars = letters + digits*numbers + special*special_characters
    pwd = ''

    while (any(d in pwd for d in digits) != numbers) and (any(s in pwd for s in special) != special_characters):
        pwd = ''.join(random.sample(chars, random.randint(min_length, min_length+10)))

    return pwd

if __name__ == '__main__':
    print(password_generator(int(input('input a minimum password length: '))))
