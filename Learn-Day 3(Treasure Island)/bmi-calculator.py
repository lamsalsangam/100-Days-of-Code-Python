weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in m: "))
bmi = round(weight/height**2, 2)
print({f"Your BMI is {bmi}."})
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight.")
elif bmi < 30:
    print("Overweight.")
elif bmi < 35:
    print("Obese.")
else:
    print("Clinically Obese.")
