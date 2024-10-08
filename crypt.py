def shift_cipher(message, shift, direction):
    result = ""
    if direction == "E":
        output_type = "encoded"
    elif direction == "D":
        shift = -shift
        output_type = "decoded"
    else:
        print("Invalid direction. Choose 'E' for encode or 'D' for decode.")
        return None, None

    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result, output_type

def get_valid_input(prompt, valid_options):
    user_input = input(prompt).upper()
    if user_input in valid_options:
        return user_input
    else:
        print(f"Invalid input. Valid options are: {', '.join(valid_options)}")
        user_input = input(prompt).upper()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input from the user, try again from the start!")
            exit()

def get_valid_shift(prompt):
    try:
        shift = int(input(prompt))
        return shift
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        try:
            shift = int(input(prompt))
            return shift
        except ValueError:
            print("Invalid input from the user, try again from the start!")
            exit()

# User input
message = input("Enter the message: ")
direction = get_valid_input("Type 'E' to encrypt, 'D' to decrypt: ", ["E", "D"])
shift = get_valid_shift("Enter the shift number: ")

# Output the result
result, output_type = shift_cipher(message, shift, direction)
if result is not None:
    print(f"The {output_type} message is: {result}")

