#1.6 Functions till now.
#3 Next number.
def next_number(number):
   
    new_number = int(number)+1
    message = 'The next number of ' + str(number) + ' is ' + str(new_number)
    return message

number = input('Enter a number: ')
print(next_number(number))