weight = float(input("enter your weight in Kilograms: "))
height = float(input("enter your height in Meters: "))

bmi= weight / height ** 2

print(bmi)
bmi_as_int = int(bmi)
print(bmi_as_int)

if bmi_as_int < 18.5:
    print("you are underweight.")
elif bmi_as_int < 25:
    print("you are a healthy weight.")
elif bmi_as_int < 30:
    print("you are overweight.")
elif bmi_as_int < 35:
    print("you are obese.")
else:
    print("you are clinically overweight.")