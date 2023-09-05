# Pgm 2 using input data in json in python

import json

input= '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Geo"
  },
  { "id" : "007",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info= json.loads(input)
print('Users:', len(info))

for item in info:
  print('name:', item['name'])
  print('id:', item['id'])
  print('Attribute:', item['x'])
