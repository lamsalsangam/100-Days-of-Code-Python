from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = (position+shift) % len(alphabet)
#         cipher_text += alphabet[new_position]
#     print(f"The cipher text is {cipher_text}")


# def decrypt(encoded_text, unshift_amount):
#     decipher_text = ""
#     for letter in encoded_text:
#         position = alphabet.index(letter)
#         new_position = (position-unshift) % len(alphabet)
#         decipher_text += alphabet[new_position]
#     print(f"The deciphered text is {decipher_text}")


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % len(alphabet)
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# if direction == "encode":
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     text = input("Type your encrypted message:\n").lower()
#     unshift = int(input("Type the unshift number:\n"))
#     decrypt(encoded_text=text, unshift_amount=unshift)
# else:
#     print("You have entered the wrong direction")
