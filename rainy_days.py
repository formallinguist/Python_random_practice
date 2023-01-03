#3.4 Rainy days
def rainy_d(days):
    list_a = days.split()
    answer = 7 - len(list_a)
    return "Numbers of weekdays without rain: " + str(answer)

days = input("On what weekdays will it rain? ")
print(rainy_d(days))