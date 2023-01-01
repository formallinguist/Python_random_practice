#2.7 Lift with while
def lift_with_while(current,target):
    a = ""
    while current != target:
        if current<target:
            a += "Floor number: " + str(current) +"\n" 
            current+=1
        else:
            a +="Floor number" + str(current) + "\n"
            current-=1
    a+="Floor number: " + str(target)
    return a

current = int(input('Current floor: '))
target = int(input('Target floor: '))

print(lift_with_while(current,target))





