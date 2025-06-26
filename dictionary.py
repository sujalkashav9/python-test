# Create a dictionary with one entry: name as key and contact number as value
dict = {"sujal": 9805806958}

# Define a function to check for a contact
def check():
    try:
        # Ask user for the name to search
        name = input("Enter the name you want to search : ")
        # Print the contact number if the name exists in the dictionary
        print(dict[name])
    except KeyError:
        # If the name is not found, display an error message
        print("Contact not found")

# Define a function to enter a new contact into the dictionary
def enter_new():
    # Ask user for a new name
    name = input("Enter the new name : ")
    # Ask user for the corresponding contact number and convert to integer
    contact = int(input("Enter the new contact : "))
    # Add the new name and contact number to the dictionary
    dict[name] = contact

# First check for a contact (might be missing initially)
check()
# Add a new contact to the dictionary
enter_new()
# Check again, possibly to verify the newly added contact
check()
