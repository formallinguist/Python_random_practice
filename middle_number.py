#3.12 Middle number
def number_info(a,b,c):
    def Average(lst_1,lst_2,lst_3):
        return (lst_1 + lst_2 + lst_3) / 3

    Avg = Average(lst_1,lst_2,lst_3)
    print(f"The average of the three numbers:{Avg}")


    def middlenumber(a, b, c):
        if a <= b <= c or c <= b <= a:
            return b
        elif b <= a <= c or c <= a <= b:
            return a
        else:
            return c

    print("Middle number:",middlenumber(a,b,c))

    def even_or_oddfunc(num):
        if num%2==0:
            print("It is an even")
        else:
             print("It is an odd")
    even_or_oddfunc(c)

numbers = input("Enter the numbers: ").split(" ")
lst_1 = int(numbers[0])
lst_2 = int(numbers[1])
lst_3 = int(numbers[2])

number_info(lst_1,lst_2,lst_3)


