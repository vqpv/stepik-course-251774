text = input()

text = text.upper()

try:
    print(text.index("А"))
except ValueError:
    print("Ни большой, ни маленькой букв А в строке нет")
