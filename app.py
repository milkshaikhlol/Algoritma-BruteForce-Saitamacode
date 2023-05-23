import itertools

# Fungsi untuk melakukan brute force pada password
def brute_force_password(password, characters):
    max_length = 10  # Panjang maksimum kombinasi karakter
    found = False

    for length in range(1, max_length + 1):
        combinations = itertools.product(characters, repeat=length)
        for combination in combinations:
            attempt = ''.join(combination)
            if attempt == password:
                print("Password ditemukan:", attempt)
                found = True
                break

        if found:
            break

    if not found:
        print("Password tidak ditemukan.")

# Main program
if __name__ == '__main__':
    password = input("Masukkan password: ")
    characters = input("Masukkan karakter yang digunakan untuk brute force (pisahkan dengan spasi): ").split()
    brute_force_password(password, characters)