print("Welcome to the tip calculator.")
chumon = float(input("Waht was the total bill? "))
tip = int(input("What percentage of tip would you like to give? 10, 12 or 15? "))
hito_bango = int(input("How many people to split the bill? "))
chumon_with_tip = round((chumon+(chumon*(tip/100)))/hito_bango, 2)
Saishu_kingaku = "{:.2f}".format(chumon_with_tip)
print(f"Each person should pay: ${Saishu_kingaku}")
