#3.5 Order Students names
def order_students_names(names_user):
    names = names_user.split()
    names.sort()
    c = ""
    for i in names:
        c += i + "\n"
    return "List of students:"  + "\n" + c


names_user= input("Students: ")
print(order_students_names(names_user))