"""
File: caesar.py
Name: Shane Liu
-------------------------
This program demonstrates the idea of "caesar cipher".
Users will be asked to input a number to produce shifted ALPHABET as the cipher table.
After that, any strings typed in will be encrypted.
"""

# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    secret_num = input('Secret number: ')
    ciphered_str = input('What\'s the ciphered string? ')
    deciphered_str = caesar(secret_num, ciphered_str)
    print('The deciphered string is: '+deciphered_str)


def caesar(secret_num, ciphered_str):
    """
    :param1 secret_num: int, a number to produce shifted ALPHABET
    :param2 ciphered_str: str, the ciphered string
    :return: str, the deciphered string
    """
    # case-insensitive
    ciphered_str = ciphered_str.upper()
    # shifted ALPHABET
    shifted_alphabet = ALPHABET[len(ALPHABET)-int(secret_num):]+ALPHABET[:len(ALPHABET)-int(secret_num)]
    
    deciphered_str = ''
    for i in ciphered_str:
        if shifted_alphabet.find(i) != -1:
            deciphered_str += ALPHABET[shifted_alphabet.find(i)]
        else:
            deciphered_str += i
    return deciphered_str


if __name__ == '__main__':
    main()
