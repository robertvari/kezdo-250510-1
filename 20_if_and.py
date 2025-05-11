# Our database
username = "csaba99"
password = "testpas123"

# Display our webshop
print("-"*50, "Wellcome to our webshop", "-"*50)
print("Please log in:")

# Get username and password from terminal
input_username = input("Username: ")
input_password = input("Password: ")


# check username and pasword
#           True                           False
if username == input_username and password == input_password:
    print("You are logged in :)))")
else:
    print("The username or password is not correct :(((")