#2.10 Steps
def steps(user):
    print("__")
    for i in range(0, int(user)-1):
        steps = ' ' + ' '*(1+i*2) + '|_'
        print(steps)
    end = "_"*(int(user)*2)+"|"
    return end

user = input("How many levels?")
print(steps(user))