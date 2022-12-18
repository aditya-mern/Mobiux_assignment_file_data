# Date,  SKU,  Unit Price,  Quantity,  Total Price                 <--Schema

# file reading
with open('sales-data.txt') as my_data:
    raw_data = my_data.readlines()

key_products = raw_data[1:]   #ignoring first row


# striping each row and spliting by comma(,)
key_products = [row.strip().split(",") for row in key_products]

# storing distinct item names
distinct_items = []
for each in key_products:
    distinct_items += [each[1]]
    
distinct_items = list(set(distinct_items))  # used set for unique item name




list1 = []
list2 = []
list3 = []
for item_name in distinct_items:       # used double loop for compairing unique names and each row of data
    quantity_count1 = 0
    quantity_count2 = 0
    quantity_count3 = 0
    revenue1 = 0
    revenue2 = 0
    revenue3 = 0

    total_sales = 0  # grand total price
    sales_month_1 = 0
    sales_month_2 = 0
    sales_month_3 = 0
    for each in key_products:
        last_value = int(each[4])                   # selecting last value for total price
        total_sales += last_value                   # updating grand total price
        month = int(each[0].split("-")[1])
        if(month == 1):                             # month wise filtering
            sales_month_1 += last_value
            if(item_name == each[1]):               # name wise filtering
                quantity_count1 += int(each[3])
                revenue1 += int(each[4])
        
        elif(month == 2):
            sales_month_2 += last_value
            if(item_name == each[1]):
                quantity_count2 += int(each[3])
                revenue2 += int(each[4])
        
        elif(month == 3):
            sales_month_3 += last_value
            if(item_name == each[1]):
                quantity_count3 += int(each[3])
                revenue3 += int(each[4])

    list1.append((item_name,quantity_count1,revenue1))    # maintaining name, quntity and revenue of each month
    list2.append((item_name,quantity_count2,revenue2))    # for further sorting
    list3.append((item_name,quantity_count3,revenue3))
        


# answer 1
print("\n")
print("Total sales of the store is:", total_sales)
print("\n")
# answer 2
print("Total sales for month 1 =",sales_month_1)
print("Total sales for month 2 =",sales_month_2)
print("Total sales for month 3 =",sales_month_3)
print("\n")
# answer 3
list1 = sorted(list1, key=lambda x: x[1], reverse = True)    # sorted by quantity (high to low)
list2 = sorted(list2, key=lambda x: x[1], reverse = True)
list3 = sorted(list3, key=lambda x: x[1], reverse = True)
print("Most popular item in month_1 is --{}-- and quantity sold is --{}--".format(list1[0][0],list1[0][1]))
print("Most popular item in month_2 is --{}-- and quantity sold is --{}--".format(list2[0][0],list2[0][1]))
print("Most popular item in month_3 is --{}-- and quantity sold is --{}--".format(list3[0][0],list3[0][1]))
print("\n")
# answer 4
list1 = sorted(list1, key=lambda x: x[2], reverse = True)    # sorted by revenue (high to low)
list2 = sorted(list2, key=lambda x: x[2], reverse = True)
list3 = sorted(list3, key=lambda x: x[2], reverse = True)
print("Item generating most revenue in month_1 is --{}-- and revenue is --{}--".format(list1[0][0],list1[0][2]))
print("Item generating most revenue in month_2 is --{}-- and revenue is --{}--".format(list2[0][0],list2[0][2]))
print("Item generating most revenue in month_3 is --{}-- and revenue is --{}--".format(list3[0][0],list3[0][2]))
print("\n")

# answer 5
# Here I,m considering ( 1 quntity = 1 order) for (min, max, avg) for most popular item
quantity_list1 = []
quantity_list2 = []
quantity_list3 = []
total_order1 = 0
total_order2 = 0
total_order3 = 0
for each in key_products:
        
    month = int(each[0].split("-")[1])
    if(month == 1):
        total_order1 += int(each[3])
        if(each[1] == "Hot Chocolate Fudge"): # used item-name, as name of most popular item is known from previous result(month wise)
            quantity_list1.append(int(each[3]))
            
    elif(month == 2):
        total_order2 += int(each[3])
        if(each[1] == "Hot Chocolate Fudge"):
            quantity_list2.append(int(each[3]))
        
    elif(month == 3):
        total_order3 += int(each[3])
        if(each[1] == "Hot Chocolate Fudge"):
            quantity_list3.append(int(each[3]))


# answer 5
print("For month_1: min = {}, max = {} and average = {} number of orders".format(min(quantity_list1),max(quantity_list1),(sum(quantity_list1)/total_order1)))
print("For month_2: min = {}, max = {} and average = {} number of orders".format(min(quantity_list2),max(quantity_list2),(sum(quantity_list2)/total_order2)))
print("For month_3: min = {}, max = {} and average = {} number of orders".format(min(quantity_list3),max(quantity_list3),(sum(quantity_list3)/total_order3)))
print("\n")


main_list = []
for item_name in distinct_items: # item wise total-sales
    total = 0
    for each in key_products:
        total_sales_of_each = int(each[4])
        if(item_name == each[1]):
            total += total_sales_of_each

    main_list.append((item_name, total))


new_list = sorted(main_list, key=lambda x: x[0]) # arranged in alphabetical order
for j in range(len(new_list)):
    print("{}) {} : {}".format(j+1,new_list[j][0], new_list[j][1]))



print("\n")
month_data = []
for i in range(1, 5): # month wise sales-data
    sales_month = 0
    for each in key_products:

        month = int(each[0].split("-")[1])
        last_value = int(each[4])

        if (i == month):
            sales_month += last_value
    month_data.append((i, sales_month))


print("Month : Total-sales")
for row in month_data:
    print("  {}   : {}".format(row[0], row[1]))