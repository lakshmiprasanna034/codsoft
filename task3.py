import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if length <= 0:
            print("Password length must be greater than 0.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}")

        generate_again = input("Do you want to generate another password? (yes/no): ").lower()
        if generate_again != 'yes':
            print('Thanks for using the password generator!')
            break

if __name__ == "__main__":
    password_generator()
