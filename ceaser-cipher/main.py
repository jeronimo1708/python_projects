from itertools import cycle
from art import logo

print(logo)

choice = ""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while choice not in ["encode", "decode"]:
    choice = input("Type 'encode' to encode a message and 'decode' to decode a message.\n").lower()
text = input(f"Type the text to {choice}\n")
shift = int(input("Type your shift number:\n"))

def encode_str(text, shift, circular_letters):
    encoded_str = ""
    for char in text:
        if not char.isalnum():
            encoded_str += char
        elif char.isdigit():
            encoded_str += char
        else:
            encoded_str += letters[letters.index(char) + shift] 
    return encoded_str

def decode_str(text, shift, circular_letters):
    decoded_str = ""
    for char in text:
        if not char.isalnum():
            decoded_str += char
        elif char.isdigit():
            decoded_str += char
        else:
            decoded_str += letters[letters.index(char) + shift] 
    return decoded_str

if choice == "encode":
    processed_text = encode_str(text, shift, letters)
else:
    processed_text = decode_str(text, shift, letters.reverse())
print(processed_text)

