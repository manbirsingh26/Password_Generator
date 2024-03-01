import random
import string


def generate_password(length=12):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length using the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_unique_passwords(num_passwords, length=12):
    # Use a set to store unique passwords
    generated_passwords = set()

    # Continue generating passwords until the desired number of unique passwords is achieved
    while len(generated_passwords) < num_passwords:
        password = generate_password(length)
        generated_passwords.add(password)

    return list(generated_passwords)


if __name__ == "__main__":
    while True:
        try:
            # Prompt the user to enter the desired password length and the number of unique passwords
            password_length = int(input("Enter the desired password length: "))
            num_passwords = int(input("Enter the number of unique passwords to generate: "))
        except ValueError:
            print("Please enter valid numeric values.")
            continue

        if password_length <= 0 or num_passwords <= 0:
            print("Please enter positive values for password length and number of passwords.")
            continue

        # Generate unique passwords
        generated_passwords = generate_unique_passwords(num_passwords, password_length)

        # Display the generated passwords
        print("\nGenerated Passwords:")
        for i, password in enumerate(generated_passwords, start=1):
            print(f"Password {i}: {password}")

        # Ask the user if they want to generate more passwords or quit
        user_input = input("\nDo you want to generate more passwords? (yes/no): ").lower()
        if user_input != 'yes':
            print("Exiting the program. Goodbye!")
            break
