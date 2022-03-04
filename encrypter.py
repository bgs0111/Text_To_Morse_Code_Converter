from ktext_splitter import *
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

K_MORSE_CODE = {
    'ㄱ': '.-..', 'ㅎ': '.---', 'ㄴ': '..-.', 'ㅏ': '.', 'ㄷ': '-...', 'ㅑ': '..', 'ㄹ': '...-', 'ㅓ': '-', 'ㅁ': '--',
    'ㅕ': '...', 'ㅂ': '.--', 'ㅗ': '.-', 'ㅅ': '--.', 'ㅛ': '-.', 'ㅇ': '-.-', 'ㅜ': '....', 'ㅈ': '.--.', 'ㅠ': '.-.',
    'ㅊ': '-.-.', 'ㅡ': '-..', 'ㅋ': '-..-', 'ㅣ': '..-', 'ㅌ': '--..', 'ㅔ': '-.--', 'ㅍ': '---', 'ㅐ': '--.-',
}

def encrypt(sentence):
    morse_output = []
    for letter in sentence:
        letter = letter.upper()
        if letter in MORSE_CODE:
            morse_output += MORSE_CODE[letter]
        elif letter == ' ':
            morse_output += " "
        elif ord('가') <= ord(letter) <= ord('힣'):
            kchar_list = decompose_korean(letter)
            for kchar in kchar_list:
                morse_output += K_MORSE_CODE[kchar]
        else:
            print("Invalid Input!")
            break

    output_to_str = ''.join(morse_output)
    return output_to_str