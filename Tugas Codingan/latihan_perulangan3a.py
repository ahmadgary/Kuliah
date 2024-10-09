a = 2
while a <= 16:
    print(a, end=", " if a < 16 else "")
    if a < 4:
        a += 1
    elif a < 8:
        a += 2
    elif a < 16:
        a += 4
    else:
        break