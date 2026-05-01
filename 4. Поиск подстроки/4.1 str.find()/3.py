s = input()

x_1 = s.find(" ")
new_s = s[x_1 + 1:]
x_2 = new_s.find(" ")

print(new_s[:x_2])
