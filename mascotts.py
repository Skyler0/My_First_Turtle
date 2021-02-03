#remove woodman
#insert bulldogs idex #4
#remove trojans 
#remove patriots
#insert trojans index #5
#insert patriots index #9


masscot_list = ["Eagles", "Warriors", "Panthers", "Tigers", "Woodmen", "Patriots", "Cougars", "Wildcats", "Knights", "Trojans"]

print("The current list is ", masscot_list)

remove = input("What masscot is incorrect ")
remove_index = masscot_list.index(remove)
masscot_list.pop(remove_index)
print("The new list is ", masscot_list)

add = input("Which masscot is missing? ")
add_index = int(input("Where should the missing masscot go? "))
masscot_list.insert(add_index, add)
print("The new list is ", masscot_list)

swap1 = input("What is the first masccot that is out of order? ")
swap2 = input("What is the second masccot that is out of order? ")
swap1_index = masscot_list.index(swap1)
swap2_index = masscot_list.index(swap2)

masscot_list.pop(swap2_index)
masscot_list.pop(swap1_index)

masscot_list.insert(swap1_index, swap2)
masscot_list.insert(swap2_index, swap1)

print("The final list is ", masscot_list) 


'''name1 = input("What is the masscot you want to remove ")
index_number = masscot_list.index(name1)
masscot_list.pop(index_number)
print(masscot_list)
masscot1 = input("What masscot do you want to input at index number 4 ")
masscot_list.insert(4, masscot1)
print(masscot_list)
name2 = input("What masscot do you want to remove to later add in a different spot? ")
name3 = input("What other masscot do you want to remove to later add in a different spot? ")
index_number = masscot_list.index(name2)
masscot_list.pop(index_number)
print(masscot_list)
index_number = masscot_list.index(name3)
masscot_list.pop(index_number)
print(masscot_list)
masscot2 = input("What masscot do you want to input at index number 5 ")
masscot_list.insert(5, masscot2)
print(masscot_list)
masscot3 = input("What masscot do you want to input at index number 9 ")
masscot_list.insert(9, masscot3)
print(masscot_list)'''