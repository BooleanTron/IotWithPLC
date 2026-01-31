from opcua import Client, ua

OPC_SERVER_URL = "opc.tcp://192.168.0.10:4840"
client = Client(OPC_SERVER_URL)
client.connect()

node2 = client.get_node("ns=4;i=25")
node1 = client.get_node("ns=4;i=24")

#value = client.get_values([node1,node2])
#print(value)
#node1.set_value(ua.DataValue(ua.Variant(2, ua.VariantType.Int16)))
#node2.set_value(ua.DataValue(ua.Variant(2.1, ua.VariantType.Float)))

#value = client.get_values([node1,node2])
#print(value)

def readInt():
    value = client.get_values([node1])
    return value

def readFloat():
    value = client.get_values([node2])
    return value

def WriteInt(intValue):
    node1.set_value(ua.DataValue(ua.Variant(intValue, ua.VariantType.Int16)))
    
def WriteFloat(FloatValue):
    node2.set_value(ua.DataValue(ua.Variant(FloatValue, ua.VariantType.Float)))



