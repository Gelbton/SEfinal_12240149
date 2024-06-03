#!/usr/bin/env python3

import requests
import json
from faker import Faker

fake = Faker()

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

def delBook(id, apiKey):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{id}", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            }
    )
    if r.status_code == 200:
        print(f"Book with ID {id} deleted.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to delete book with ID{book}.")

# Get the Auth Token Key
apiKey = getAuthToken()

def getBookCount():
    r = requests.get(
        f"{APIHOST}/api/v1/books"
    )
    if r.status_code == 200:
        return 40   # placeholder value for efficiency sake


# Using the faker module, generate random "fake" books
# fake = Faker()
bookcount = getBookCount()
decrBookcount = bookcount-5

for i in range(0, 5):
    delBook(i, apiKey)

for i in range(decrBookcount, bookcount):
    print(getBookCount)
    delBook(i, apiKey)
