import urllib
import urllib.parse
import urllib.request
import sqlite3
import json
import time
import ssl
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')
fh = open("where.data")
count = 0
for line in fh:
    if count > 200:
        break
    address = line.strip()
    print('')

    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (address.encode(), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database", address)
    except:
        print('Resolving', address)
        url = serviceurl + urllib.parse.urlencode({"sensor": "false", "address": address})
        print('Retrieving', url)

        try:
            uh = urllib.request.urlopen(url, context=scontext)
            data = uh.read()
            print('Retrieved', len(data), 'characters', data[:20].decode('utf-8').replace('\n', ' '))

            count = count + 1
            try:
                js = json.loads(data.decode('utf-8'))
                # print js  # We print in case unicode causes an error
            except:
                continue

            if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
                print('==== Failure To Retrieve ====')
                print(data)
                break

            cur.execute('''INSERT INTO Locations (address, geodata)
                    VALUES (?, ?)''', (address.encode(), data))
            conn.commit()
            time.sleep(1)
        except Exception as e:
            print('Error:', e)


print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
