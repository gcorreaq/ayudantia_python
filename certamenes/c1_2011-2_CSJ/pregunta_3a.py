word = raw_input("Palabra abreviada: ")

final_word = ''

for i in range(0, len(word), 2):
    numero = int(word[i])
    final_word += (word[i + 1] * numero)

print final_word