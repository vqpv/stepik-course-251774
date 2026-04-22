message = input()
cipher = input()
plain = input()

translation_table = str.maketrans(cipher, plain)

print(message.translate(translation_table))
