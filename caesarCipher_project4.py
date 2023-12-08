alphabets = 'abcdefghijklmnopqrstuvwxyz'
alphabets_list = list(alphabets)

def text_encryption_and_decryption(user_choice, message, shift_key):
    if user_choice == 'decrypt':
        shift_key *= -1 
    new_text = ''
    for ch in message:
        if ch in alphabets:
            new_text += alphabets_list[(alphabets_list.index(ch) + shift_key) % 26]
        else:
            new_text += ch
    if user_choice == 'encrypt':
        print(f"Encrypted text of '{message}' is '{new_text}'")

    elif user_choice == 'decrypt':
        print(f"Decrypted text of '{message}' is '{new_text}'")

stop = False
while not stop:
    user_choice = input("Type 'encrypt' for encryption, type 'decrypt' for decryption: ")
    if user_choice != 'encrypt' or user_choice != 'decrypt':
        print('Wrong user choice.')
        break
    text = input('Type your message: ').lower()
    shift = int(input('Enter shift key: '))
    text_encryption_and_decryption(user_choice, text, shift)
    play_again = input("Type 'yes' to continue, 'no' to exit: ")
    if play_again == 'no':
        stop = True



