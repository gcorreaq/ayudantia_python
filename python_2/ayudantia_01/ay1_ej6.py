num_1 = int(raw_input('Num 1: '))
num_2 = int(raw_input('Num 2: '))
num_3 = int(raw_input('Num 3: '))

if num_1 < num_2:
    if num_1 < num_3:
        # ya sabemos que num_1 es el menor
        print num_1,

        if num_2 < num_3:
            print num_2, num_3
        else:
            print num_3, num_2
    elif num_3 < num_2:
        print num_3, num_1, num_2
elif num_2 < num_3:
    # num_2 es el menor de todos
    print num_2,

    if num_3 < num_1:
        print num_3, num_1
    else:
        print num_1, num_3
elif num_3 < num_1:
    # num_2 es el menor
    print num_2,

    if num_3 < num_1:
        print num_3, num_1
    else:
        print num_1, num_3
