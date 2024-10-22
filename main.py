# Lincoln Walker

def encode(password):
    encoded_password = ""
    for x in password:
        for _ in range(3):
            if x == "9":
                x = "0"
            else:
                x = str(int(x) + 1)
        encoded_password = encoded_password + x
    return encoded_password


def decode(password):
    pass


if __name__ == "__main__":
    while True:
        print("\n1. Encode\n2. Decode\n")
        selection = int(input("Menu Selection: "))

        if selection == 1:
            print(f"\nEncoded Password: {encode(input("Password: "))}")
        elif selection == 2:
            print(f"\nDecoded Password: {decode(input("Password: "))}")
        else:
            print("Invalid Selection")
