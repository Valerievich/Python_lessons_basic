# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    digits = 10 ** ndigits
    number = digits * number
    if int((number * 10) % 10) >= 5:
        return int(number + 1)/digits
    else:
        return int(number)/digits

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    my_tuple = tuple(map(int, ticket_str))
    n = len(ticket_str) // 2
    return sum(my_tuple[:n]) == sum(my_tuple[n:])


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
