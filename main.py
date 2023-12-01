# Создаем программный файл F1 и записываем в него построчно данные, вводимые пользователем
with open('F1.txt', 'w') as file:
    while True:
        data = input("Введите данные: ")
        if data == "":
            break
        file.write(data + '\n')

# Копируем из файла F1 в файл F2 строки, в которых есть слова, совпадающие со вторым словом
with open('F1.txt', 'r') as file1, open('F2.txt', 'w') as file2:
    for line in file1:
        words = line.split()
        if len(words) > 1 and words1.isalpha():  # Проверяем наличие второго слова в строке
            file2.write(line)

# Определяем количество цифр в последней строке файла F2
with open('F2.txt', 'r') as file:
    lines = file.readlines()
    lastline = lines[-1]
    digitcount = sum(c.isdigit() for c in lastline)
    print("Количество цифр в последней строке файла F2:", digitcount)