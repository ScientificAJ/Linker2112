import pandas
import csv
location = input("Location Of The File: ")
link = ""
with open(location) as file:
    dorks = csv.reader(file, delimiter=",")
    
    
    
    listoflinks = []
    listoflinks2 = []
    for i in file:
        i = i.replace("[", "").replace("]", "").replace("'", "")
        listoflinks.append(i)
    
    for i in listoflinks:
        i = "inurl:" + i

 


        listoflinks2.append(i)

    


for i in listoflinks2:
    i = i.replace("\n", "")
    link += i + " | "
link = link[:-2]
print(link)


        
        
        
