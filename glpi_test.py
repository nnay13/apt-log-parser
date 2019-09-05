import json
import requests

user_token = "wfiob2csi6mnoira912rm414008lohikx2903l3lq"
app_token = "ubm8bDJJ3SuSoNqITgMWo9NakcQ1ANsTcqb0C0ZI"
glpi_url = "http://10.100.101.54/glpi/apirest.php"

headers = {"Content-Type": "application/json",
           "Authorization":"user_token "+ user_token,
           "App-Token": app_token }

url = glpi_url+"/initSession"

req = requests.get(url, headers=headers)

print(headers)

print(req.content)
