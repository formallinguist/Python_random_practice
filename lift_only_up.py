#2.4 Lift only up
def lift_only_up(current,target): 
    for number in range(int(current), int(target)+1):
       print('Floor number: '+ str(number))

current = input('Current floor: ')
target = input('Target floor: ')

lift_only_up(current,target)