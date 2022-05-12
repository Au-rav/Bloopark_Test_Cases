import xml.etree.cElementTree as ET

tree = ET.ElementTree(file='Question3\input.xml')

root = tree.getroot()

for child in root:
    if child.tag=="food":
        for attr in child:
            print(attr.text)
    
