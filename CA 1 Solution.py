### Question 1 (55 marks)
"""
The Northwind data set, provided in XML format on Moodle, includes details of employees, customers,
products and sales for a fictitious company.

- (a) Create a function to import this XML file. Your function must include appropriate exception
    handling clauses covering all possible error conditions and should return the parsed contents of the
    XML file. [15 marks]
    
- (b) Using the function you created in a) above, load the XML file. Then use the print() function to
    display the ProductName and UnitPrice for the 2, 4, 6, 8 and 10 products.
    Hint: the range() function might come in useful here! [15 marks]
"""

# import xml lib
import xml.etree.cElementTree as ET

# parse xml file in the tree format
tree = ET.parse('NorthWind.xml')

#load the root of the tree i.e <northwind>
root = tree.getroot()

# As mentioned in b we have to print for no: 2,4,6,8 and 10 products
mylist = [2,4,6,8,10]


for child in root :
    if child.tag == 'Products':
        for grandchild in child:
            product_id = int(grandchild.get('ProductID'))
            if product_id in mylist:
                print("Product ID : ", product_id)
                print("Product Name : ", grandchild.find('ProductName').text)
                print("Unit Price :", grandchild.find('UnitPrice').text)
