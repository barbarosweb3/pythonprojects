print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

result = round((bill / people * 1.10), 2)
result1 = round((bill / people * 1.12), 2)
result2 = round((bill / people * 1.15), 2)

if tip == 10:
    print(f"Each person should pay: ${result:.2f}")
elif tip == 12:
    print(f"Each person should pay: ${result1:.2f}")
elif tip == 15:
    print(f"Each person should pay: ${result2:.2f}")
else:
    print("The process couldn't be completed! (Panic!)")