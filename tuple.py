username = ('jai','sumit','abhinav','sujal','rishi')
password = (13,69,43,45,65)

enter_user = input("Enter your username : ")
enter_pass = int(input("Enter your pass : "))
ans = False
for i in range (len(username)):
    if(enter_user == username[i] and enter_pass == password[i]):
        ans = True
        break
       
       
if (ans == True):
    print("correct")
else:
    print("wrong")
