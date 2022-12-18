#1.10 Inhabitants
def inhabitants(place):
    if place =='Donostia':
        return 'Hello Donostiar'
    elif place == 'Aberdeen':
        return  'Hello Aberdonian'
    elif place == 'Istanbul':
        return 'Hello, Istanbulite'
    elif place == 'Sydney':
        return 'Hello, Sydneyite'
    else:
        return "I'm Sorry, I donot know your town...."

place = input('Where are you from? ')

print(inhabitants(place))