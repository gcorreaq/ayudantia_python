word = raw_input("Palabra: ")

size = len(word)
j = size - 1

success = True

for i in range(j / 2):

    if word[i] == ' ':
        i += 1
        j += 1
    elif word[j] == ' ':
        j -= 1
        i -= 1
    elif word[i] != word[j]:
        print 'No es palindromo'
        success = False
        break

    # Esto podria estar en un else
    j -= 1

if success:
    print 'Es palindromo'
