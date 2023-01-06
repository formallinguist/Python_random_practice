#5.1 Scrabble game.
def scrabble_game(user):
    total=0
    with open("points_eu.txt") as f:
        for line in f:
            (key, val) = line.split()
            #print(key,val)
            if val.lower() in user:
               # print(val,key)
                total+=int(key)
    total1=0
    with open("points_en.txt") as f1:
        for line in f1:
            (key, val) = line.split()
            #print(key,val)
            if val.lower() in user:
               # print(val,key)
                total1+=int(key)
    return total,total1

word = input("word: ")
b,e= scrabble_game(word)
print(f"points in Basque {b}")
print(f"points in english {e}")