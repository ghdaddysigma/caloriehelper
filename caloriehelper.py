import colorama
from colorama import Fore, Style

gender = input("Enter your gender: ").strip().lower()
weight = float(input("Enter your weight in kg: ").strip())
height = float(input("Enter your height in cm: ").strip())
age = int(input("Enter your age: ").strip())
activity_level = input("Enter your activity level on a scale of 1 to 5: ").strip()

if gender == 'male':
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
elif gender == 'female':
    bmr = 10 * weight + 6.25 * height - 5 * age - 161
else:
    print("Invalid gender. Please enter 'male' or 'female'.")
    exit()

if activity_level == '1':
    print(Fore.BLUE + "==============================================")
    print("You should eat", bmr * 1.2, "a day")
    print(Fore.BLUE + "==============================================")
    print("Your BMR is: ", bmr)
    print(Fore.BLUE + "==============================================")
elif activity_level == '2':
    print(Fore.BLUE + "==============================================")
    print("You should eat", bmr * 1.375, "a day")
    print(Fore.BLUE + "==============================================")
    print("Your BMR is: ", bmr)
    print(Fore.BLUE + "==============================================")
elif activity_level == '3':
    print(Fore.BLUE + "==============================================")
    print("You should eat", bmr * 1.55, "a day")
    print(Fore.BLUE + "==============================================")
    print("Your BMR is: ", bmr)
    print(Fore.BLUE + "==============================================")
elif activity_level == '4':
    print(Fore.BLUE + "==============================================")
    print("You should eat", bmr * 1.725, "a day")
    print(Fore.BLUE + "==============================================")
    print("Your BMR is: ", bmr)
    print(Fore.BLUE + "==============================================")
elif activity_level == '5':
    print(Fore.BLUE + "==============================================")
    print("You should eat", bmr * 1.9, "a day")
    print(Fore.BLUE + "==============================================")
    print("Your BMR is: ", bmr)
    print(Fore.BLUE + "==============================================")
else:
    print("Invalid activity level. Please enter a number between 1 and 5.")
    exit()