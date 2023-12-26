import itertools

# Function to brute force passwords
def brute_force_password(password, characters):
    max_length = 10  # Maximum length of character combination
    found = False

    for length in range(1, max_length + 1):
        combinations = itertools.product(characters, repeat=length)
        for combination in combinations:
            attempt = ''.join(combination)
            if attempt == password:
                print("detected password: ", attempt)
                found = True
                break

        if found:
            break

    if not found:
        print("Password not found!")

# Main program
if __name__ == '__main__':
    password = input("Enter password: ")
    characters = input("Enter the characters for brute force (separate them with spaces): ").split()
    brute_force_password(password, characters)
