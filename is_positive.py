#1.8 positive
def is_positive (number):
    if number >= 0:
        return 'The entered number is positive'
    else:
        return 'The entered number is not positive'
number = input('Enter a number: ')
print(is_positive(int(number)))