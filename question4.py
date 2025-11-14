#question 5 MTn Mobile Mobile Transaction

amount = float(input("Enter amount to send: "))

if amount <= 100:
    charge = 2
elif amount <= 500:
    charge = 5
else:
    charge = 10
final = amount - charge
print(f"Amount Sent: GHS {amount}")
print(f"Charge: GHS {charge}")
print(f"Receiver Gets: GHS {final}")
