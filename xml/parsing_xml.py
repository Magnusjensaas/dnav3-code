from xml.dom import minidom

myxml = minidom.parse("converting_json_xml.xml")

pool = myxml.getElementsByTagName("pool")

for elem in pool:
    print(elem.firstChild.data)


