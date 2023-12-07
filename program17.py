#The basic outline of this problem is to read the file, look for integers #using the re.findall(), looking for a regular expression of '[0-9]+' and then #converting the extracted strings to integers and summing up the integers.
import re

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_42.txt"

fh = open(fname)
li=list()
for lines in fh:
    listnum=re.findall('[0-9]+',lines)
    for num in listnum:
        li.append(int(num))
print(sum(li))
    

    
    
    