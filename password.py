# 1.7 Password.
def password(pin):
    if pin == 'kukuakEgitenDuKuku' :
        return 'Access allowed'
    else:
        return 'Access denied'

pin = input("Enter the password: ")

print(password(pin))