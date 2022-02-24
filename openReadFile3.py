"""Задача 3. Напишите функцию, которая берёт содержимое файла,
заменяет все символы пробела на символ нижнего подчеркивания "_".
Получившуюся строку сохраните в новом файле."""

def newSim(file):
    file = open(file)
    file_txt = file # сохранил файл в другую переменную что бы закрыть его
    file2 = open('newDefFileItWordsTestik.txt', 'w')
    file = file.read().replace(".", "...")
    file2.write(file)
    file_txt.close()
    print('Файл создан!')
    return file2


newSim()
