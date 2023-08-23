#Pgm to add a number a find average using making a list and add value using append func.

numlist=list()
while True:
  inp=input('Enter a number:')
  if inp=='done': 
    break
  value=float(inp)
  numlist.append(value)
average=sum(numlist)/len(numlist)
print('Average:', average)
