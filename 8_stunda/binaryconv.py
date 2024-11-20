a = input("> ")
if not a.isdigit():
    print("Invalid input")
    exit()
else:
    a = int(a)

output = ""

while 1:
    s = a % 2
    a = a // 2
    output = str(s) + output
    if a == 0:
        break

print(output)
