#pgm using for loop, None value and is as operator to find the count and smallest number 

zork=0
smallest=None
print('before', zork)
for thing in [9,13,7,20,4,23,55]:
  if smallest is None:
    smallest=thing
  elif thing<smallest:
    smallest=thing
  zork=zork+1
  print('count:',zork,thing)
  print('Smallest:',smallest)
print('After', zork, 'smallest:', smallest)
