text = input()
substr = input()

print((len(text) - len(text.replace(substr,""))) // len(substr))
