#2.2 Cheer leader
def cheerleader(team):
    answer = ''
    for i in team:
        answer = answer + 'Give me a(n)' + str(i)+', ' +str(i) +'! \n'   
    spelling = answer + "What's that spell? \n" +  str(team).upper() + '! ' +str(team).upper() + '!'
    return spelling 
team = input('Your team: ')
message = (cheerleader(team))        
print(message)

