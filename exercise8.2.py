#Pgm to read data from mbox-short.txt and slice it and read lines starting with from 
#and print the day from the'From' lines

han=open('mbox-short.txt')

for line in han:
  line=line.rstrip()
  #print('line:',line)
  wds=line.split()
  #print('Words:', wds)
  #Gaurdian in compound statement 
  if len(wds)<3 or wds[0]!='From':
   # print('Ignore:')
    continue
  print(wds[2])  
