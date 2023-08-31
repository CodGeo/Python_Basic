# Pgm to create a simple we browser using urllib in python.

import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
  print(line.decode().strip())
