age = input("What is your current age? ")

year_days = 365
year_weeks = 52
year_months = 12

total_years = 90
int_age = int(age)
final_age = total_years - int_age
final_age_days = final_age*year_days
final_age_weeks = final_age*year_weeks
final_age_months = final_age*year_months

print(
    f"You have {final_age_days} days or {final_age_weeks} weeks or {final_age_months} months left")
