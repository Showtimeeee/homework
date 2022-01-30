inp = ''
summa = 0
while inp.isdigit:
    print('Введите число: ', end='')
    inp = input()
    if inp == 'q':
        break
    summa += int(inp)
print(summa)



