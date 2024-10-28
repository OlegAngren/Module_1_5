# Создание неизменяемого кортежа (immutable)
immutable_var = (1, 2, 'a', 'b')
print("Неизменяемый кортеж:", immutable_var)

# Попытка изменить элементы кортежа
# immutable_var[0] = 10  # Эта строка вызовет ошибку TypeError

# Объяснение: Кортежи (tuple) в Python являются неизменяемыми объектами, что значит, что после их создания
# изменить элементы внутри кортежа невозможно. Это свойство обеспечивает безопасность данных.

# Создание изменяемого списка (mutable)
mutable_list = [1, 2, 'a', 'b']
print("Изменяемый список:", mutable_list)

# Изменение элементов списка
mutable_list[1] = 'Изменение'  # Изменение второго элемента
mutable_list.append('Новый элемент')  # Добавление нового элемента в конец списка
print("Список после изменений:", mutable_list)