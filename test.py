import xml.etree.ElementTree as ET

tree = ET.parse("people.xml")

root = tree.getroot()

print(root.tag)