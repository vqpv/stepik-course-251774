s = input()

t = str.maketrans("", "", ".,!?;:-")
s = s.translate(t)

while "  " in s:
    s = s.replace("  ", " ")

print(s.count(" ") + 1)
