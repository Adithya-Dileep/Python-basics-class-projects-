height = float(input('Enter the height in meters'))
weight = float(input('Enter the weight in kg'))
BMI = weight/(height*height)
if BMI < 18.5: 
    print('You are under weight')
elif BMI >= 18.5 and BMI <= 24.9:
    print('You normal weight')
elif BMI >= 25 and BMI <= 29.9:
    print('You are overweight')
else:
    print('You are obese')