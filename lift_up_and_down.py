#Lift up and down
def lift_up_and_down(current,target):
    answer = " "
    if current < target:
        for number in range(int(current), int(target)+1):
          answer = answer +  '\nFloor number: ' + str(number)
    elif current > target:
        for number in range(int(current), int(target)-1,-1):
            answer = answer + '\nFloor number: ' + str(number)
    
    return answer
    


current = input('Current floor: ')
target = input('Target floor: ')

print(lift_up_and_down(current, target))
