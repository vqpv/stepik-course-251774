s = input()

try:
    print(s[:s.index(".")])
except ValueError:
    print("Неверный формат даты")
