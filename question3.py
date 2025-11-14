
#question 1 TroTro fare Calculator
print("=== TroTro Fare CALCULATOR ===")

route = input("Enter your route (Madina/Kasoa/Tema): ").lower()
passengers = int(input("How many passengers? "))
if route == "madina":
    fare = 5

elif route == "kasoa":
    fare = 10
elif route == "tema":
    fare = 8
else:
    print("Invalid route selected!")
    exit()
total = fare * passengers
print(f"total fare for {passengers} passengers is:GHS {total}")


