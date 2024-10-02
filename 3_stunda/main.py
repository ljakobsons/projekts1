import math

prices = input("").split(" ")
prices = [int(x) for x in prices]

prices.sort(reverse=True)
itemAmount = len(prices)
finalSum = 0

triples = math.floor(itemAmount / 3)
splitPrices = []


def sort_index(lst, rev=True):
    index = range(len(lst))
    s = sorted(index, reverse=rev, key=lambda i: lst[i])
    return s


for i in range(triples):
    l = prices[:3]
    splitPrices.append(l)
    for p in l:
        prices.remove(p)

print(splitPrices)
print(prices)

for t in splitPrices:
    finalSum += t[0]
    finalSum += t[2]

for i in prices:
    finalSum += i

print(f"Final sum for all items: {finalSum}")
