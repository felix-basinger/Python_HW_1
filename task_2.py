# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал
# каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза
# больше журавликов, чем Петя и Сережа вместе?

figures_count = int(input("Enter the count of figures: "))
sergey = figures_count
petr = figures_count
katya = (sergey + petr) * 2
result = sergey + petr + katya
print(f"{result} -> {petr} {katya} {sergey}")
