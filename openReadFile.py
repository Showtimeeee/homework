"""Задача 1. Напишите программу, которая открывает текстовый файл
 и выводит на экран его содержимое."""

file = open('sieson 42(ftp.ru).txt', 'r')
data = file.read()
print(data)
file.close()

