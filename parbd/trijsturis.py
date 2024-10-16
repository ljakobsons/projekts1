from time import sleep

a = float(input("> "))
b = float(input("> "))
c = float(input("> "))

lst = [a, b, c]
lst.sort(reverse=True)

if not lst[2] + lst[1] >= lst[0]:
    print("Nevar izveidot trīsstūri")
else:
    if lst[2] ** 2 + lst[1] ** 2 == lst[0] ** 2:
        print("Var izveidot taisnlenķa trīsstūri")
    elif lst[2] ** 2 + lst[1] ** 2 >= lst[0] ** 2:
        print("Var izveidot šaurlenķa trīsstūri")
    elif lst[2] ** 2 + lst[1] ** 2 <= lst[0] ** 2:
        print("Var izveidot platlenķa trīsstūri")

sleep(10)