#4.5 Shout requests
def shout_requests(file):
    answer = open(file)
    a = ""
    for line in answer:
        a+= line.upper()
  
    answer.close()
    return a
    
   

print(shout_requests("requests.txt"))

