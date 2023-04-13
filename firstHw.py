import requests
import re
from datetime import datetime

while (True):
    try:
        countParas = int(input("How many paragraph are you want? (FYI: count of paragrahps cannot be less 5): "))
        if 5 <= countParas:
            break
        else:
            print("You must enter a number equal to or greater than 5")
    except ValueError:
        print("You don`t input number or input text!")

request = requests.get("https://baconipsum.com/api/?type=meat-and-filler&format=text&paras="+str(countParas))
text = re.split(r"\n{2,}", request.text)
text.reverse()
countRepeat = 0

for i,v in enumerate(text):
    if re.search(r"Pancetta", v):
        countRepeat +=1

with open("homework1", "w") as f:
    f.write("Student: Gerzhan Vlad\n")
    f.write("Date: " + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")
    f.write("Count paragraphs with word \"Pancetta\": " + str(countRepeat) + "\n")
    for par in text:
        f.write(par + "\n")

print("Success!")