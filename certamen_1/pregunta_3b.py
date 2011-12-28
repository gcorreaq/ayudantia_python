word = raw_input("Palabra abreviada: ")

stop = len(word)
actual_char = 0
final_word = ''

while actual_char < stop:
	repetitions = int(word[actual_char])
	actual_char += 1

	final_word += word[actual_char] * repetitions
	actual_char += 1

print final_word