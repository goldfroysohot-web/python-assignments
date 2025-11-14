
# Question5 Voting Eligibility System


name = input("Enter your name: ")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").lower()

if age >= 18 and nationality == "ghanaian":
  print(f"{name}, you are ELIGIBLE to vote in Ghana.")
elif age < 18 and nationality == "ghanaian":
  print(f"{name}, you are NOT ELIGIBLE to vote . You must be at least 18 years old to vote")
elif age >= 18 and nationality != "ghanaian":
  print(f"{name}, you are NOT ELIGIBLE to vote in Ghana. You must be a Ghanian citizen to vote.")
else:
  print(f"{name}, you are NOT ELIGIBLE to vote in Ghana.")