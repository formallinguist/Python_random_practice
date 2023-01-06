# 5.2 User names 
import csv
def username(filename):
    l=[]
    with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=' ')
            row=[row for row in reader]
            p=""
            c=1
            for i in range(1,len(row)):
                        k=row[i][0].lower().replace(" ", "")
                        if k in l:
                                if  k+row[i][1][0].lower() ==p:
                                    l.append(k+row[i][1][0].lower()+str(c))
                                    c+=1

                                else:
                                    l.append(k+row[i][1][0].lower())
                                    p=k+row[i][1][0].lower().replace(" ", "")
                                    c=1
                        else:

                                l.append(row[i][0].lower().replace(" ", ""))
                                st = "\n".join(l)
                         #print(row[i][0].lower())
            return st

print(username('class_list.csv'))

