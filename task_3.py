# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.

print_num = input("Enter your number: ")
if len(print_num) != 6:
    print("Error! Incorrect data")
else:
    num = int(print_num)
    count_1 = 0
    count_2 = 0

    new_num = num % 1000
    num = num // 1000

    while num > 0:
        new_numb = num % 10
        count_1 += new_numb
        num = int(num / 10)

    while new_num > 0:
        new_numb = new_num % 10
        count_2 += new_numb
        new_num = int(new_num / 10)

    if count_1 == count_2:
        print(f"{print_num} -> yes")
    else:
        print(f"{print_num} -> no")
