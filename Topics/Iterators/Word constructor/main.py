word_1 = input()
word_2 = input()
brand = ''
for a, b in zip(word_1, word_2):
    brand += a + b
print(brand)
