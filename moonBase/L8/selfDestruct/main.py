# Write a script that makes HTTP requests to the server
# http://127.0.0.1:8082/selfdestruct until the numbers match
# and read the response to get the flag.
# You can easily run out of execution time in this challenge.
# You will need to check the response and stop your attack
# once you see the flag.

import urllib.request

url = "http://127.0.0.1:8082/selfdestruct"

while True:
    # if response contains "try again" then continue
    response = urllib.request.urlopen(url).read()
    #print(response)
    if "try again".encode() in response:
        print("fail")
        continue
    else:
        print("success")
        print(response)
        break
    