import math

prices = input("> ").split(" ")
print("\n")
prices = [int(x) for x in prices]

prices.sort(reverse=True)
itemAmount = len(prices)
finalSum = 0

triples = math.floor(itemAmount / 3)
splitPrices = []

for i in range(triples):
    maxp = prices[:2]
    minp = prices[-1]

    splitPrices.append([maxp[0], maxp[1], minp])
    prices.remove(maxp[0])
    prices.remove(maxp[1])
    prices.remove(minp)

print(splitPrices)
print(prices)

for t in splitPrices:
    finalSum += t[0]
    finalSum += t[2]

for i in prices:
    finalSum += i

print("\n")
print(f"Final sum for all items: {finalSum}")
