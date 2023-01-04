#4.4 Words Frequency.
def words_frequency():
    user = input("Enter a line: ")
    dictionary = {}
    variable = ""
    while user != "":
        words = user.split() 
        for element in words:
            if element not in dictionary:
                dictionary[element]=1
            else: 
                dictionary[element] = dictionary[element]+1
        user=input("Enter a line: ")
    for i in sorted(dictionary): 
        variable+= i +" "+ str(dictionary[i]) + "\n"
    return variable.strip()

print(words_frequency())