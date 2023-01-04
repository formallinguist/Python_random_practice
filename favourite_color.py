#4.2 Favourite colour
def favourite_colour():
    agenda = {}
    line=input("Name and colour: ")
    while line:
        name,colour = line.split()
        agenda[name] = colour
        line=input("Name and colour: ")
    variable=""    
    for name in sorted(agenda):
        variable+= name + " "+ agenda[name] + "\n"
    
    return variable.strip() 

print(favourite_colour())
