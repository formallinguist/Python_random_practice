#1.6 Functions till now
#4 year of birth
def year_of_birth(age):
    year = 2021
    year_of_birth = int(year) - int(age)
    answer = 'You were born in ' + str(year_of_birth) +"."
    return answer
age = input('How old are you? ')
print(year_of_birth(age))