phonebook = {}

# add item to dictionary
phonebook["06 20 123 4567"] = {"name": "Csaba", "address":"Budapest"}
phonebook["06 20 123 5464"] = {"name": "Kriszta", "address":"Pécs"}

# update/edit item in dictionary
phonebook["06 20 123 4567"]["name"] = "Béla"
print(phonebook)