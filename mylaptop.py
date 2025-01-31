import os
os.system("cls" if os.name=="nt" else "clear")

laptop = { "brand": "dell", "model": "alienware", "year": 2010}

print("Laptop Brand:", laptop["brand"])

laptop["home"] = True 

print("Updated Laptop Info:", laptop)

laptop["year"] = 2019

print("Laptop Info After Year Update:", laptop)
