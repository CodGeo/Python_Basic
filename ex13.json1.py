# Pgm using JSON in python

import json

data= '''
{
  "name" : "Geo",
  "phone" : {
    "type" : "intl",
    "number" : "+919446707090"
  },
  "email" : {
    "hide" : "yes"
  }
}'''

info=json.loads(data)
print('name:',info["name"])
print('email:',info["email"]["hide"])
