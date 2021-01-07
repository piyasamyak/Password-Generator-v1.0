import random
import logos
from password_characters import alphabets, symbols, numbers

print(logos.logo)
print("Welcome to the Password Generator v1.0 by Samyak Piya (SaPi)!\n")

# Generates given number of characters for each string type
def generate_password_string(num_of_type, type_of_char):
    password_of_type = ""
    for i in range(num_of_type):
        password_of_type += random.choice(type_of_char)
    return password_of_type


# Generates a new password by randomizing the sequence of characters in the combined password
def generate_password(combined_password_strings):
    combined_password_strings_list = list(combined_password_strings)
    randomized_password_list = random.sample(
        combined_password_strings_list, len(combined_password_strings_list)
    )
    password = "".join(randomized_password_list)
    return password


num_of_alphabets, num_of_symbols, num_of_numbers = [], [], []
num_of_chars = [num_of_alphabets, num_of_symbols, num_of_numbers]
continueGenerating = True
passwords = []

while continueGenerating:
    num_alphabets = int(input("How many alphabets do you want in your password?\n-> "))
    num_symbols = int(input("\nHow many symbols do you want in your password?\n-> "))
    num_numbers = int(input("\nHow many numbers do you want in your password?\n-> "))
    print()

    num_of_alphabets.append(num_alphabets)
    num_of_symbols.append(num_symbols)
    num_of_numbers.append(num_numbers)

    # Combining different characters types into one string
    combined_password = (
        generate_password_string(num_alphabets, alphabets)
        + generate_password_string(num_symbols, symbols)
        + generate_password_string(num_numbers, numbers)
    )

    # Randomizes the seuqence of the characters in the combined password
    password = generate_password(combined_password)

    create_another = input(
        f"The unique password you generated is as follows: {password}\nIt is {len(password)} characters long. Do you want to generate another password? Type 'yes' or 'no':\nNote: The password(s) you created so far will be saved and accessible at the end.\n-> "
    ).lower()

    while create_another != "yes" and create_another != "no":
        create_another = input(
            "\n---Invalid input. Please enter 'yes' to generate another password or 'no' to stop.---\n-> "
        )

    if create_another == "no":
        continueGenerating = False
    elif create_another == "yes":
        print()

    # Adds password(s) the user created to a list
    passwords.append(password)


print(f"\n{logos.thanks}\n")
print(
    f"You have generated {len(passwords)} password(s) in total. You may store them somewhere safe. They are as follows:\n"
)
for each in range(len(passwords)):
    print(
        f"{each + 1}: {passwords[each]} ({len(passwords[each])} characters long: '{num_of_chars[0][each]}' alphabet(s), '{num_of_chars[1][each]}' symbol(s), and '{num_of_chars[0][each]}' number(s).)"
    )
