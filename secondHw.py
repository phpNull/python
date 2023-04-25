import requests
import re
import time

def requestLink(sleepSecond, link):
    for i,v in enumerate(link):
        responseData = requests.get(str(v), timeout=sleepSecond)
        if 200 == responseData.status_code:
            print(v + str("\n"))

links = []
while (True):
    temp = None
    temp = input("Input link for GET query or leave blank if you want to finish typing: ")

    if 0 < len(links) and temp == '':
        break
    elif not re.search(r"^[http?s://, ]", temp):
        print("start with http:// or https://")
    elif 0 == len(links) and temp == '':
        print("Insert at least one link") 
    else:
        links.append(temp)
        

while (True):
    try:
        cntSecond = int(input("Input count seconds for sleep before send query: ") or 0)
        break
    except ValueError:
        print("You must input number!")

requestLink(cntSecond, links)