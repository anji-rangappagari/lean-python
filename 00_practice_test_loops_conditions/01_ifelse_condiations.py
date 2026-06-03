age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult and you are eligible to vote: Positive")
elif age >= 18 and age < 21:
    print("You are an adult but will schedule a call to review your eligibility: Pending/Zero")
else:
    print("You are a minor: Negative")

print("Voter eligibility check is complete.")