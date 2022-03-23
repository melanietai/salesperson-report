"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] # empty list to contain names of salespeople
melons_sold = [] # empty list to contain numbers of melon sold for each salesperson

f = open('sales-report.txt')

# for line in f:
#     line = line.rstrip() # remove whitespace to the right
#     entries = line.split('|') # tokenize items in line split by |
#     salesperson = entries[0] # get name of salesperson
#     melons = int(entries[2]) # get number of melons sold for that sales person

#     if salesperson in salespeople: # if salesperson's name found in salespeople list
#         position = salespeople.index(salesperson) # find the index of that name inside list
#         melons_sold[position] += melons # find corresponding melons sold and add to the amount of melons sold
        
#     else:
#         salespeople.append(salesperson) # append new name to the salesperson list
#         melons_sold.append(melons) # append number of melons sold to melons sold list


# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons') # print name and melons sold

# this provide two separate lists, but since its mutable, the index position for each item might change
# it would be better to store the information in a dictionary with key-value pair
# salesperson name as key and melons sold as value
# can use dict.item() to print out both keys and values

salesperson_melons = {}

for line in f:
    line = line.rstrip()
    entries = line.split('|')

    salesperson_melons[entries[0]] = salesperson_melons.get(entries[0], 0) + int(entries[2])

for name, melons_sold in salesperson_melons.items():
    print(f'{name} sold {melons_sold} melons')
