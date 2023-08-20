#Pgm to compute the pay of employees 1.5 times the hourly using def functions (computepay)

hrs=input('Please enter your Hours:')
rate=input('Please enter your Hourly rates:')
try:
  hrs1=float(hrs)
  rate1=float(rate)
except:
  print('Error, Please enter numeric input.')
  quit()
def computepay(hours,rate):
  if hours>40:
    print('Overtime')
    reg=hours*rate
    otp=(hours-40.0)*(rate*0.5)
    pay=reg+otp
    print('Your Pay is:',pay)
  else: 
   print('Regular')
   pay=hours*rate
   print('Your Pay is:',pay)
computepay(hrs1,rate1)    
print('All Done')
