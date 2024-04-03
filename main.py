import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

if response.status_code == 200:
    print("Success")
else:
    if response.status_code == 404:
        print("Not Found")
    else:
        print("Failed")
