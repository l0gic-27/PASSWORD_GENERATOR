import random
import string

def generate_password(length=12):

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():

    length = int(input("Enter the length of the password: "))

    password = generate_password(length)

    print("Generated Password:", password)

if __name__ == "__main__":
    main()
