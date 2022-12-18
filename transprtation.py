#1.11 Transportation.
def transportation(distance):
    if distance =='Yes':
        return 'Better go by bus.'
    if distance =='No':
      distance_1 = int(input('How many kilometers is the workplace? ')) 
      if distance_1 > 10 :
        return "Take the bus."
      elif distance_1 >=2 and distance_1 <=10:
        return 'Better to ride a bike.'
      elif distance_1 <2:
         return "Better to walk."

distance = input('is it raining? ')


print(transportation(distance))