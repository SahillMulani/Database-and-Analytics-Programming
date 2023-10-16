### Question 1 (55 marks)
"""
The Northwind data set, provided in XML format on Moodle, includes details of employees, customers,
products and sales for a fictitious company.

- (a) Create a function to import this XML file. Your function must include appropriate exception
    handling clauses covering all possible error conditions and should return the parsed contents of the
    XML file. [15 marks]
    
- (b) Using the function you created in a) above, load the XML file. Then use the print() function to
    display the ProductName and UnitPrice for the second, fourth, sixth, eighth and tenth products.
    Hint: the range() function might come in useful here! [15 marks]
"""

import xml.etree.cElementTree as ET

tree = ET.parse('NorthWind.xml')

root = tree.getroot()

mylist = [2,4,6,8,10]

for value in root :
    if value.tag == 'Products':
        for child in value:
            product_id = int(child.get('ProductID'))
            if product_id in mylist:
                print("Product ID : ", product_id)
                print("Product Name : ", child.find('ProductName').text)
                print("Unit Price :", child.find('UnitPrice').text)
