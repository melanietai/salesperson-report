"""Generate sales report showing total melons each salesperson sold."""


# salespeople = [] # empty list to contain names of salespeople
# melons_sold = [] # empty list to contain numbers of melon sold for each salesperson

# f = open('sales-report.txt')

# for line in f: # loop over each line in file object
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

def get_melons_sold_by_salesperson(log_file_path):
    """Return a dictionary of {salesperson_name: melons_sold}.

    Arguments:
        log_file_path (str) - the path to a sales report log file

    Return:
        salesperson_melons (dict)
    """

    salesperson_melons = {}

    with open(log_file_path) as f:

        for line in f:
            line = line.rstrip()

            # create a list of data and unpack its values
            salesperson_name, total_dollars, melons_sold = line.split('|') 

            # set or increment the saleperson's total melons sold
            salesperson_melons[salesperson_name] = salesperson_melons.get(salesperson_name, 0) + int(melons_sold)

    return salesperson_melons

def print_sales_report(melons_by_salesperson_dict):
    """Print a report of salespeople and the total number of melons they've sold.
    
    Arguments:
        melons_by_salesperson_dict (dict) - {salesperson_name: melons_sold}
    """

    for name, melons_sold in melons_by_salesperson_dict.items():
        print(f'{name} sold {melons_sold} melons')

print_sales_report(get_melons_sold_by_salesperson('sales-report.txt'))
