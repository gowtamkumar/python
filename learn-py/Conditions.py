age = 20
if age >= 18:
    print("You are eligible to vote.")
else:
    print("you are not eligible to vote.")

score = 75

if score >= 80:
    print("You got an A+ grade.")
elif score >= 70:
    print("You got a A Grade.")
elif score >= 60:
    print("You got a B Grade.")
elif score >= 50:
    print("You got a C Grade.")
else:
    print("You got a D Grade.")
    
    
seat_type = input("Enter seat type (sleeper/AC/general/Luxury)")

match seat_type:
    case "sleeper":
        print("You have selected Sleeper class.")
    case "AC": 
        print("You have selected AC class.")
    case "general":
        print("You have selected General class.")
    case "Luxury":
        print("You have selected Luxury class.")
    case _:
        print("Invalid seat type selected.")
        
        
    
   