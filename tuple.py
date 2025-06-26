# Tuple of valid usernames
username = ('jai', 'sumit', 'abhinav', 'sujal', 'rishi')

# Tuple of corresponding passwords (must match index-wise with usernames)
password = (13, 69, 43, 45, 65)

# Taking input from the user for username
enter_user = input("Enter your username : ")

# Taking input from the user for password and converting it to integer
enter_pass = int(input("Enter your pass : "))

# Variable to track if login is successful
ans = False

# Looping through the list of usernames
for i in range(len(username)):
    # Check if both username and password match at the same index
    if (enter_user == username[i] and enter_pass == password[i]):
        ans = True  # If match found, set ans to True
        break       # Exit the loop since user is authenticated

# Final check to print result based on ans value
if (ans == True):
    print("correct")  # Login successful
else:
    print("wrong")    # Login failed
