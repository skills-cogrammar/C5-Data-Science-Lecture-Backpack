'''
Code a Python program that will read from the text file inventory.txt and
perform the following on the data, to prepare for presentation to your
managers:
o Create a file named inventory.py, where a Shoe class should be
defined.
o In the Shoe class, create a function (read_data()) that will
implement a try-except block for reading the following information
from the file:
● country,
● code,
● product,
● cost, and
● quantity.
o Create at least 5 shoe objects and store these in a list. Add
functionality to search products in the objects list by code.
o Write code to determine the product with the lowest quantity, and
restock it.
o Write code to determine the product with the highest quantity and
mark it up as being for sale.
o You will have noticed that in the original data, there are only five
columns. Write a function, value_per_item(), to calculate the value
(or total worth) of each item entered. (Please keep the formula for
value in mind; value = cost * quantity.) This function should then
create a sixth column for each product, named value.
'''




class Shoe:
    
    def __init__(self, country, code, prod, cost, qty):
        
        self.country = country
        self.code = code
        self.prod = prod
        self.cost = cost
        self.qty = qty
        
    def convert_to_int(self):
        
        self.qty = int(self.qty)
        
    def adjust_qty(self, new_qty):
        
        self.qty = new_qty

    def put_on_sale(self, sale_value):
        
        self.cost = sale_value
    
    def __str__(self):
        
        return f"""
Country : {self.country}
Code : {self.code}
Product : {self.prod}
Cost : {self.cost}
Quantity : {self.qty}
"""

#file = open("inventory.txt", "r")
shoe_data = []

def read_data():
    
    with open('inventory.txt', 'r') as file:
    
        for lines in file:
            data = lines.strip().split(',')
            
            if "Country" not in data:
                shoe_data.append(Shoe(data[0],data[1],data[2],data[3],data[4]))
                
                
def find_lowest_qty():
    
    qty_list = []
    for idx in shoe_data:
        
        idx.convert_to_int()
        qty_list.append(idx.qty)

    lowest = min(qty_list)
    print(lowest)
    
    adjustment = input("To what value would you like to restock : ")
    
    for idx in shoe_data:
        
        idx.convert_to_int()
        
        if idx.qty == lowest:
            print(idx)
            
            idx.adjust_qty(adjustment)
            print(f"Adjusted : \n{idx}")

read_data()
find_lowest_qty()