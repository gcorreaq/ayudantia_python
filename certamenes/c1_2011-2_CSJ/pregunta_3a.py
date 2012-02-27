word = raw_input("Palabra abreviada: ")

actual_char = 0
final_word = ''

for i in range(len(word)/2):
	repetitions = int(word[actual_char])
	actual_char += 1

	final_word += word[actual_char] * repetitions
	actual_char += 1

print final_word