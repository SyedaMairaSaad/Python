#9.4 Write a program to read through the mbox-short.txt and figure out who has #sent the greatest number of mail messages. The program looks for 'From ' lines #and takes the second word of those lines as the person who sent the mail. The #program creates a Python dictionary that maps the sender's mail address to a #count of the number of times they appear in the file. After the dictionary is #produced, the program reads through the dictionary using a maximum loop to #find the most prolific committer.
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
    
    if 'From:' not in lines:
        continue
    elif 'From:'  in lines[0]:
        #print(lines)
        lines=lines[1]
        listEmail[lines]=listEmail.get(lines,0)
        if lines in listEmail:
            listEmail[lines]=listEmail[lines]+1
        
    #print(bigCount)
    for k,v in listEmail.items():
        #print(v);
        if bigCount is None or v>int(bigCount):
            bigCount=v
            bigWord=k
        

print(bigWord,bigCount)
