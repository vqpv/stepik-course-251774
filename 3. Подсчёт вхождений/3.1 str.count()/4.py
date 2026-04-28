text = input()
word = input()

text = text.upper()
word = word.upper()

c = 0

while word in text:
    c += text.count(word)
    text = text.replace(word, "")

print(c)
