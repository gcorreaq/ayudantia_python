word = raw_input("Palabra: ")

size = len(word)
j = size - 1

success = True

for i in range(j / 2):

    if word[i] != word[j]:
        print 'No es palindromo'
        success = False
        break

    j -= 1

if success:
    print 'Es palindromo'
