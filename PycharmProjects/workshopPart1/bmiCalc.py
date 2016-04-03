print('Body-mass-index calculator, by John Kanekunga')

weight = float(input('Please enter your weight in kgs:'))
height = float(input('Please enter your height in m:'))

bmi = weight / (pow(height, 2))

print('Therefore, your BMI value is:', bmi, '\nthankyou!')