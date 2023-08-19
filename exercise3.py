#Pgm to compute the pay of employees 1.5 times the hourly rates if hours worked is > 40

hrs=input('Please enter your Hours:')
rate=input('Please enter your Hourly rates:')
hrs1=float(hrs)
rate1=float(rate)
if hrs1>40:
  print('Overtime')
  ot=hrs1-40
  ot1=float(ot)
  pay=(40*rate1)+((ot1*1.5)*10)
  print('Your Pay is:',pay)
else: 
  print('Regular')
  pay=hrs1*rate1
  print('Your Pay is:',pay)
  
print('All Done')
