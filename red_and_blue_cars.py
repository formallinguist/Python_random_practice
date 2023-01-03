#3.9 Red and Blue cars
def red_and_blue_cars(cars):

    cars.strip(str(not('red' + 'blue')))
    red = cars.count('red' or 'red ')
    blue = cars.count('blue')

    return red,blue

cars = input('Cars: ')
x,y = red_and_blue_cars(cars)
print("Red:", x)
print("Blue:", y)




