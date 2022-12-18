#1.9 Positive and even.

def positive_and_even(number):
    if number >= 0:
        if number%2 == 0:
            return 'The number entered is positive and even'
        if number%2 == 1:
            return 'The number entered is positive and odd'
    else:
        return 'The number entered is not positive'
number = int(input('Enter a number: '))
print(positive_and_even(number))   