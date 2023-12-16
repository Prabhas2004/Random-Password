import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the length of the password: "))
        if password_length <= 0:
            print("Password length must be greater than 0.")
        else:
            password = generate_password(password_length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
