#2.9 Look for factors
def look_for_factors(number):
    number_i = int(number)
    variable = ""
    for element in range(1,number_i+1):
        if number_i % element==0: 
            variable+= str(element)+"\n" 
    return variable.strip() 
number = input("Enter a number: ")

print(look_for_factors(number))
