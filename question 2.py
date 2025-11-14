
# Question 3:Cocoa Farm yield Estmator

bags = int(input("Enter number of cocoa bags harvested: "))

income = bags * 850
if bags > 100:
    income += 2000

print(f"Total income: GHS {income}")


