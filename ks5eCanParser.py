import cantools
import can
from pprint import pprint
import matplotlib.pyplot as plt
dbc = cantools.database.load_file('Orion_CANBUS.dbc')
dbc.add_dbc_file('20200701_RMS_PM_CAN_DB.dbc')
cantools.database.dump_file(dbc,"ks5e.dbc")
print(dbc)
ks5edbc = cantools.database.load_file('ks5e.dbc')
ks5edbc.refresh()
can_bus = can.interface.Bus('vcan0',bustype='socketcan')
while(True):
    message=can_bus.recv()
    print(ks5edbc.decode_message(message.arbitration_id,message.data))
