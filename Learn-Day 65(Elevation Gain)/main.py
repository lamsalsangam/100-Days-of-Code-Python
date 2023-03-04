def elevationgain():
    elevation=[]
    climbing= True
    while climbing:
        user_input=int(input("Enter the point  where you are at in meters: "))
        elevation.append(user_input)
        choice=(input("Are there any other point for climbing (Type 'Y' or  'N'): ")).upper()
        if choice=="N":
            climbing = False

    print(elevation)
    result=calculate(elevation)
    print(f"Total elevation gain is {result}")
            
def calculate(points):
    sumation= 0
    for i in range(len(points)-1):
        sum = points[i+1]-points[i]
        if sum > 0:
            sumation +=sum
    return sumation


elevationgain()