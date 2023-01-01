#2.6 Double factorial.
def double_factorial(num):
    count = 1
    for i in range (num, 0, -2):

        count*= i
    answer = "Double factorial:" + str(count)
    return answer
    
num = int(input("Enter a number: "))
print(double_factorial(num)) 