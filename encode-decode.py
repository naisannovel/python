def encrypt():
    encoded_message = ''
    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            encoded_message += alphabet[new_position]
        else:
            encoded_message += letter
    print(f'your encoded message is {encoded_message}')


def decrypt():
    decoded_message = ''
    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift
            decoded_message += alphabet[new_position]
        else:
            decoded_message += letter
    print(f'your decoded message is {decoded_message}')


program_running = True
while program_running:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    convert_type = input('What type you want to convert? "encode" or "decode"\n').lower()
    if convert_type == "encode" and convert_type == "decode":
        message = input('Enter your message\n').lower()
        shift = int(input('How many shift you want?\n')) % 26
        if convert_type == "encode":
            encrypt()
        elif convert_type == "decode":
            decrypt()
    else:
        print('you can convert only encoded and decoded')

    is_running = input('do you want continue this program? "yes" or "no"\n').lower()
    if is_running == "no":
        program_running = False
