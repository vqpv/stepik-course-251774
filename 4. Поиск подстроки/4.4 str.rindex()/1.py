s = input()

try:
    i_1 = s.index("(")
    i_2 = s.rindex(")")
    if i_2 > i_1:
        print(s[i_1 + 1:i_2])
    else:
        print("Ссылка не найдена")
except ValueError:
    print("Ссылка не найдена")
