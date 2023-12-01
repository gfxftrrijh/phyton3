# Создаем программный файл prices.txt и записываем в него построчно данные, вводимые пользователем
with open('prices.txt', 'w') as file:
    while True:
        data = input("Введите данные (название, количество, стоимость за единицу через пробел): ")
        if data == "":
            break
        file.write(data + '\n')

# Определяем общую стоимость заказа
total_cost = 0
with open('prices.txt', 'r') as file:
    for line in file:
        data = line.split()
        quantity = int(data[1])
        price = float(data[2].replace(',', '.'))  # заменяем запятую на точку для корректного перевода в число
        total_cost +=  price

print("Общая стоимость заказа:", total_cost)