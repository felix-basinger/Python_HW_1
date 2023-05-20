# Задача 2: Найдите сумму цифр трехзначного числа.

num = int(input("Enter the three-digit number: "))
count = 0
if num > 999 or num < 100:
    print("Error. It's not three-digit number")
else:
    while num > 0:
        new_num = num % 10
        count += new_num
        num = int(num / 10)
    print(count)
