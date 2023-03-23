from urllib import request
import json

url = "http://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
print(r.getcode())
data = r.read()
jsonData = json.loads(data)
print(jsonData)