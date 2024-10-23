# Lincoln Walker

def encode(password):
    encoded_password = ""
    for x in password:
        for _ in range(3):
            if x == "9":
                x = "0"
            else:
                x = str(int(x) + 1)
        encoded_password += x
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for x in encoded_password:
        for _ in range(3):
            if x == "0":
                x = "9"
            else:
                x = str(int(x) - 1)
        decoded_password += x
    return decoded_password

if __name__ == "__main__":
    encoded_password = ""
    original_password = ""
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            original_password = input("Please enter your password to encode: ")
            encoded_password = encode(original_password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            if encoded_password:
                print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}")
            else:
                print("No password has been encoded yet.")
        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")
