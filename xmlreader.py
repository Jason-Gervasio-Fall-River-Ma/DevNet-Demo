import xmltodict

with open("r1.xml", "r") as file:
    xml_data = file.read()

data = xmltodict.parse(xml_data)
print(data)