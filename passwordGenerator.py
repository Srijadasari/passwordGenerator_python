import random
import string

def generate_password(length):
    # Ensuring the password has a mix of all character types
    if length < 4:  # Minimum length for a mix of character types
        print("Password length should be at least 4 for a secure mix.")
        return None

    # Define character pools
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password with a balanced mix of characters
    password = [
        random.choice(string.ascii_uppercase),  # at least one uppercase letter
        random.choice(string.ascii_lowercase),  # at least one lowercase letter
        random.choice(string.digits),           # at least one digit
        random.choice(string.punctuation)       # at least one special character
    ]

    # Fill the remaining length with random characters from all pools
    password += [random.choice(all_characters) for _ in range(length - 4)]
    
    # Shuffle the list to randomize character positions
    random.shuffle(password)

    return ''.join(password)

def main():
    # Prompt the user to enter the password length
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length must be at least 4 for a secure password.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    # Generate and display the password
    password = generate_password(length)
    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
