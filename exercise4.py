#Pgm to work out exercise 3 but using try and except

hrs=input('Please enter your Hours:')
rate=input('Please enter your Hourly rates:')
try:
  hrs1=float(hrs)
  rate1=float(rate)
except:
  print('Error, Please enter numeric input.')
  quit()
if hrs1>40:
  print('Overtime')
  ot=hrs1-40
  ot1=float(ot)
  pay=(40*rate1)+((ot1*1.5)*10)    # or pay=(hrs1*rate1)+(ot1*(0.5*rate1))
  print('Your Pay is:',pay)
else: 
  print('Regular')
  pay=hrs1*rate1
  print('Your Pay is:',pay)
  
print('All Done')
