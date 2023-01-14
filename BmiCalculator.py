# Description: It is just simple BMI Calculator 👇
# 🚨 Do not rely on it

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#TypeConversion/TypeCast
new_height = float(height)
new_weight = int(weight)

#MathematicalCalculation (BMI = Weight (in kg) / (height * height))

bmi = (new_weight / (new_height * new_height))

#Converting Decimal to Whole Number 
bmi_as_int = int(bmi)

#Print Result
print(bmi_as_int)
