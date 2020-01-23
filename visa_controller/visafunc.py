import visa
from datetime import datetime

global visa_scope

def connect_VISA():
    global visa_scope
    rm = visa.ResourceManager()
    instruments = rm.list_resources()
    usb = list(filter(lambda x: 'USB' in x, instruments))
    print(usb)
    if len(usb) != 1:
      print('Bad instrument list', instruments)
      return -1
    visa_scope = rm.open_resource(usb[0])
    return 0

def measure_IDN():
    query_out = visa_scope.query("*IDN?")
    print(query_out)
    return query_out

def measure_VPP():
    print(visa_scope.write(":MEASure:ITEM VPP,CHANNel1\n"))
    print(visa_scope.write(":MEASure:ITEM? VPP,CHANNel1\n"))
    query_out = visa_scope.read()
    print(query_out)
    return query_out