from encrypter import encrypt

user_input = input("Morse code Converter\nType text you want to encode\n")

result = encrypt(user_input)
print(f"The sentence {user_input} Converted!")
print(f"Encoded Code \n {result}")
