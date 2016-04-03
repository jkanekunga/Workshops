
def main():

    area = Calculate_Area()
    fathrenheit = convert_C_to_F()
    bmi = calculate_BMI()

    print ("Area is: {} /n Ferrnite is: {} /n MBI is: {}", format(area, fathrenheit, bmi),sep='')

#print('Area Volume and Calculator')

def Calculate_Area():
    width = float(input('Enter width:'))
    height = float(input('Enter height:'))
    #depth = float(input('Enter depth:'))

    area = width * height

    return area
main()
    #volume = area * depth
    #print('Area:', area, ' Volume:', volume)


def convert_C_to_F():
    celsiusValue = float(input('Enter celcius value:'))
    fathrenheitValue = celsiusValue * 9 / 5 + 32

    return fathrenheitValue
    #kelvinValue = celsiusValue + 273.15
main()

def calculate_BMI():
    weight = float(input('Please enter your weight in kgs:'))
    height = float(input('Please enter your height in m:'))

    bmi = weight / (pow(height, 2))

    return bmi
main()
#print('Therefore, your BMI value is:', bmi, '\nthankyou!')