def ejercicio():


    c = 0
    i = 0
    v = 0
    while(c < 5):
        v += 1
        if(c == 4):
            c = 0
            i += 1

            if(i == 3):
                c = 5
        c += 1

    print(c)
    print(i)
    print(v)

ejercicio()
