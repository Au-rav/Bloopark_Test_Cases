import xml.etree.ElementTree as ET

mytree = ET.parse('./Question3/input.xml')
myroot = mytree.getroot()

for food in myroot.iter('food'):
    price_ele = ET.Element("price")
    price_ele.text = str("50.0")
    if food.find("item").text == "Idly":
        price_ele.text = str("10")
    food.append(price_ele)

mytree.write("./Question3/output.xml")
