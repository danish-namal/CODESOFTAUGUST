import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("===================")
    
    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Please enter a valid length (greater than 0).")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number for the length.")
        return

    password = generate_password(length)
    print("Generated Password: " + password)

if __name__ == "__main__":
    main()
