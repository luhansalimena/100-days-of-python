# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2

def printResponse(result):
  print(f"Your BMI is {bmi}, you {result}.")

if(bmi < 18.5):
  printResponse("you are underweight")
elif(bmi >= 18 and bmi < 25):
  printResponse("have a normal weight")
elif(bmi >= 25 and bmi < 30):
  printResponse("are slightly overweight")
elif(bmi >= 30 and bmi < 35):
  printResponse("are obese")
elif(bmi >= 35):
  printResponse("are clinically obese")