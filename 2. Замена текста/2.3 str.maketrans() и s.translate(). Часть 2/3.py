s = input()

translation_table = str.maketrans("бвгджзклмнпрстфхцчшщБВГДЖЗКЛМНПРСТФХЦЧШЩаА", "ггггггггггггггггггггГГГГГГГГГГГГГГГГГГГГыЫ", "йЙ")

print(s.translate(translation_table))
