#4.3 cars colours.
def cars_colours():
    agenda = {}
    car = input("Car: ")
    datos = ""
    while car != "": 
        if car not in agenda:
            agenda[car] = 1
        else:
            agenda[car] = agenda[car]+1
        car=input("Car: ")
    for i in sorted(agenda, key = agenda.get,reverse=True):
        datos+= i + " cars: " + str(agenda[i]) + "\n"
    return datos.strip()

print(cars_colours())
