# Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Enter the length of chocolate bar: "))
m = int(input("Enter the width of chocolate bar: "))
k = int(input("Enter your count of chocolate bar's slices : "))

res = n * m
if k % n == 0 and k < res:
    print(f"{n} {m} {k} -> yes")
elif k % m == 0 and k < res:
    print(f"{n} {m} {k} -> yes")
elif k == res:
    print("It's whole chocolate bar")
else:
    print(f"{n} {m} {k} -> no")
