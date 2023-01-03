#3.7 Total Spent
def total_spent(money_input):
    variable = money_input.split()
    sum = 0
    for i in variable:
        sum+=int(i)
    return "Total: " + str(sum) + "$"

money_input = input("Enter the spent money: ")
print(total_spent(money_input))

