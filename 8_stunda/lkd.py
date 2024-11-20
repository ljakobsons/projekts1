a = input("Enter the first number: ")
b = input("Enter the second number: ")

if not a.isdigit() or not b.isdigit():
    print("Invalid input")
    exit()
else:
    a = int(a)
    b = int(b)

if a == 0 or b == 0:
    print("Greatest common divisor: 0")
    exit()

while 1:
    s = a % b
    if not s:
        break
    a = b
    b = s

print(f"Greatest common divisor: {b}")
