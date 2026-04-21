text = input()
old = input()
new = input()

text = " " + text + " "
old = " " + old + " "
new = " " + new + " "

new_text = text.replace(old, new)

print(new_text.strip(" "))
