list = [11,12,13,14,15]
print(list)

# using operation of stack in list
#push:
list.append(16)
print(list)
#pop:
list.pop()
print(list)
#peek:
if list:  
    last_element = list[len(list)-1]  
    print(last_element)
else:
    print("The list is empty.")
