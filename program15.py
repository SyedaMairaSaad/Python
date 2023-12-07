#10.2 Write a program to read through the mbox-short.txt and figure out the #distribution by hour of the day for each of the messages. You can pull the #hour out from the 'From ' line by finding the time and then splitting the #string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, #sorted by hour as shown below.
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
listEmail=dict()
bigCount=None
bigWord=None
for lines in fh:
    count=count+1
    lines=lines.strip()
    lines=lines.split()
    #print(lines)
    if 'From' not in lines:
        continue
    elif 'From'  in lines[0]:
        timeVariable=lines[5]
        hr=timeVariable.split(':')
        #print(hr)
        lines=hr[0]
        listEmail[lines]=listEmail.get(lines,0)
        if lines in listEmail:
            listEmail[lines]=listEmail[lines]+1
        
ls=sorted([(k,v) for (k,v) in listEmail.items()],reverse=False)
for k,v in ls:
    print(k,v)

    
    
    