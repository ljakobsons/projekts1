from math import sqrt, prod

data = open("6_stunda/teksta-faili/dati_2.txt", "rt", encoding="utf-8")

numbers = [float(x.replace("\n", "").replace(",", ".")) for x in data.readlines()]

print(f"Failā ir {len(numbers)} skaitļi.")
print(f"Skaitļu vidējā vērtība ir {sum(numbers)/len(numbers)}.")
print(f"Skaitļu vidējā ģeometriskā vērtība ir {prod(numbers)**(1/len(numbers))}.")
print(f"Skaitļu vidējā aritmētiskā vērtība ir {sum(numbers)/len(numbers)}.")
