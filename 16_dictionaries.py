#         key       :     value
phonebook = {
    "06 20 123 4567": {"name": "Kiss Csaba", "address": "Budapest"}, 
    "06 30 987 6543": {"name": "Kocsis Krisztina", "address": "Pécs"}, 
    "06 20 756 9382": {"name": "Nagy Balázs", "address": "Debrecen"},
    "06 20 758 9684": {"name": "Németh Attila", "address": "Miskolc"}
}

print(phonebook["06 30 987 6543"]["name"])
print(phonebook["06 30 987 6543"]["address"])