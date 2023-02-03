import json
import requests
from pprint import pprint
from dataclasses import dataclass, field

# api/user -> DRF

# Get -> retrieve
# Post -> create
# Patch -> partial update
# Put -> update
# Delete -> delete

# Status Code
# 1xx -> Information
# 2xx -> Success
# 3xx -> Redirection
# 4xx -> Client Error
# 5xx -> Server Error

url = "https://dummyjson.com/users"


# url = "https://google.com"

# JSON :
# dict => Object
# tuple, list => Array
# int, float => Number
# str => String
# True, False => true, false
# None => null

# data = requests.get(url).json()
# pprint(data)

# with open("url.html", "w") as f:
#     print(req.content, file=f)

def get_ip():
    # return requests.get("https://icanhazip.com").text.strip()
    return requests.get("http://ip-api.com/json").json()


# pprint(get_ip())


# class User:
#     def __init__(self, name, id, age, phone):
#         self.name = name
#         self.id = id
#         self.age = age
#         self.phone = phone

@dataclass(eq=True, order=True)
class User:
    name: str
    id: int
    age: int
    phone: str | int

    def profile(self):
        return f"""
            Name: {self.name}
            ID: {self.id}
            Age: {self.age}
            Phone: {self.phone}
        """


reza = User("Reza", 1421, 34, 989134567899)
# print(reza.profile())
# reza.id = 4545
# print(reza.profile())

class Human:
    ...


from typing import List

print(isinstance(List, object))

# class Person:
#     def __init__(self, ):