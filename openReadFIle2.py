"""Задача 2. Программа открывает текстовый файл, читает его содержимое.
Пишет содержимое в другой файл,
но все символы текста из первого файла должны быть в верхнем регистре."""

file = open('new_sieson.txt', 'r')
data = file.read()
with open('new3_upper_sieson.txt', 'w') as file:
    data_upper = data.upper()
    file.write(data_upper)
    print(data_upper)


file.close()

