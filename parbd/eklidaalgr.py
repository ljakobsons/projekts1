num1 = int(input("1st > "))
num2 = int(input("2nd > "))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(f"LKD({num1}, {num2}) = {gcd(num1, num2)}")
