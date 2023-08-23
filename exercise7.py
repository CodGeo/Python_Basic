#Pgm to to read through a file and read through the contents and print all in upper case

fh=open('mbox-short.txt')
for lx in fh:
  ly=lx.rstrip()
  print(ly.upper())
  
