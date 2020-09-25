weight = input("Enter your weight: ")
weight_type = input("If pounds type an (L), if kilograms type a (K)").lower()

if weight_type == "l":
    converted_weight = int(weight) / 2.205
    print(f"You weigh {converted_weight} Kg")
elif weight_type == "k":
    converted_weight = int(weight) * 2.205
    print(f"You weigh {converted_weight} lbs")
else:
    print("You did not enter a valid type of weight")


