#pgm to read the numbers enterd until user enters "done".
#Once "done" is entered print out the total, count and average.Use try and except

num=0
tot=0.0
while True:
  sval=input('Enter a number:')
  if sval=='done':
    break
  try:
    fval=float(sval)
  except:
    print('Invalid Input')
    continue
  num=num+1
  tot=tot+fval
print('Count:',num,'Total:',tot,'Average:',tot/num)  
