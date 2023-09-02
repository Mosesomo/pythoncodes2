# Python program to encode and decode a message for security

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                 ]


def caeser_cipher(text_message, shift_number, method):
    cipher_txt = ""
    if method == "decode":
        shift_number *= -1;
    for char in text_message:
        if char in alphabet_list:
            position = alphabet_list.index(char)
            new_position = position + shift_number
            new_text = alphabet_list[new_position]
            cipher_txt += new_text
        else:
            cipher_txt += char
    print("Here is {}d result and the  text message is {}".format(method, cipher_txt))


should_continue = True
while should_continue:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 25

    caeser_cipher(text, shift, choice)

    result = input("Type 'yes' if you want to go again. otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Good bye :)")
