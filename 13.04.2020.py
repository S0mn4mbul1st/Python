fruits = { "apple", "apple", "banana", "watermelon"}

print(fruits)

fruits.remove("banana")

print(fruits)

fruits.add("Nar")

print(fruits)


print("****************************")


def yaz():

    print("Hello World!")

yaz()

import random
import urllib.request
def ran(url):

    rand = random.randrange(1,100)

    print(rand)

    name = str(rand) + ".jpg"

    urllib.request.urlretrieve(url, name)

    print(name)

#ran("https://images.unsplash.com/photo-1531804055935-76f44d7c3621?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80")


print("****************************")

doc = open("text.txt", "w")

doc.write("Hello World lan!\n")

doc.close()

print("****************************")

read = open("text.txt", "r")

str = read.read()

print(str)

read.close()

print("****************************")

from urllib import request

def download(url):

    link = urllib.request.urlopen(url)

    csv = link.read()

    st = str(csv)

    lines = st.split("\\n")

    gog = r'google.csv'

    doc = open(gog, "w")

    for l in lines:

     doc.write(l + "\n")

    doc.close()

#download("https://query1.finance.yahoo.com/v7/finance/download/AMZN?period1=1555171253&period2=1586793653&interval=1d&events=history")

print("****************************")

while True:
  try:

        io = int(input("Enter a number:"))

        print(io)

        break

  except ValueError:

        print("Enter number")

print("****************************")