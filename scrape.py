import requests
import urllib.request

class Person(object):
    img: ""
    height: ""
    weight: ""

links = []
people = []

with open("links.txt") as f:
    for line in f:
        links.append(line)

x = 1
for link in links:

    if x > 484:
        pass
    page = requests.get(link).text
    heightData = page.split('<label for="Height:_">Height: </label>')[1].split("</div>")[0].strip()
    height = heightData[0] + " feet " + heightData[7] + heightData[8] + " inches"

    weight = page.split('<label for="Weight:_">Weight: </label>')[1].split("</div>")[0].strip()

    img = "https://apps.polkcountyiowa.gov" + page.split('<div class="col-md-3">')[1].strip().split('<img src="')[1].split('"')[0]

    person = Person()

    person.height = height
    person.weight = weight
    person.img = img

    people.append(person)
    print("located person " + str(x))
    x += 1


i = 484
for person in people:
    height = person.height
    weight = person.weight
    img = person.img
    meta= open("data/meta/" + str(i) + ".txt","w+")
    meta.write(height + "," + weight)
    meta.close

    urllib.request.urlretrieve(img, "data/img/" + str(i) + ".jpg")
    i += 1
    print("Got person " + str(i) + " of " + str(len(people)))