#1.6 Functions till now.
#5 degree calculator
def degree_calculator(celcius):
    
    fahrenheit = (float(celcius)*9/5)+32
    degree = str(fahrenheit) + ' Fahrenheit'
    return degree

celcius = input('How many Celsius? ')
print(degree_calculator(celcius))