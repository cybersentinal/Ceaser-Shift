def shift_cipher(message, shift, direction):
    result = ""
    if direction == "E":
        shift_direction = shift
        output_type = "encoded"
    elif direction == "D":
        shift_direction = -shift
        output_type = "decoded"
    else:
        print("Invalid direction. Choose 'E' for encode or 'D' for decode.")
        return None, None

    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_direction) % 26 + start)
        else:
            result += char

    return result, output_type

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).upper()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Valid options are: {', '.join(valid_options)}")

def print_all_shifts(message, direction):
    print(f"\nAll possible {direction.lower()} results from shifts 1 to 26:")
    for shift in range(1, 27):
        result, _ = shift_cipher(message, shift, direction)
        print(f"Shift {shift}: {result}")

# User input
message = input("Enter the message: ")
direction = get_valid_input("Type 'E' to encrypt, 'D' to decrypt: ", ["E", "D"])

# Output the results for all possible shifts
print_all_shifts(message, direction)
