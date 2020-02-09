from xml.dom import minidom

myxml = minidom.parse("converting_json_xml.xml")

pool = myxml.getElementsByTagName("pool")

for elem in pool:
    print(elem.firstChild.data)


xmlString = "<server><pool>http</pool><description>My virtual server test</description><name>http-virtual</name><mask>255.255.255.255</mask><profiles><name>http</name><kind>ltm:virtual:profile</kind><name>tcp</name><kind>ltm:virtual:profile</kind></profiles><ipProtocol>tcp</ipProtocol><sourceAddressTranslation><type>automap</type></sourceAddressTranslation><kind>tm:ltm:virtual:virtualstate</kind><destination>1.1.1.3</destination></server>"
dom = minidom.parseString(xmlString)
xml = dom.toprettyxml()
print(xml)





