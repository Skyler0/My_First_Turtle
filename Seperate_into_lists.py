numbers_list = [10400, 10660, 12285, 12480, 13118, 13832, 14560, 17045, 17521, 17680, 18200, 18718, 19054, 20839, 21359]
thirteen_list = []
seven_list = []
both_list = []
for number in numbers_list:
    if (number % 7 == 0):
        seven_list.append(number)
    elif(number % 13 == 0):
        thirteen_list.append(number)
    if (number % 7 == 0): 
        if (number % 13 == 0):
            both_list.append(number)
print("These numbers are divisible by 7", seven_list, "These numbers are divisible by 13", thirteen_list, "These numbers are divisible by both seven and thirteen", both_list) 