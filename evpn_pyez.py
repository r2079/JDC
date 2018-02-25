

#Simple Program to print EVPN Type2 and Type3 Routes
import os
from jnpr.junos import Device as dev
from jnpr.junos.op.routes import RouteTable as r #OP Module to get the Route Information from the Device
list_of_devices = ['192.168.0.83','192.168.0.84']
for i in range(len(list_of_devices)):
    d = dev(host=list_of_devices[i],user='lab',password='lab123')
    print "#-------Evpn Route Information for Device {}".format(list_of_devices[i])
    print "\n"
    d.open()
    r_list = r(d).get() #Helps to get the Items from the Route-Table
    keylist = r_list.keys() #Keys in Route-Table Output
    valuelist = r_list.values() #Values in Route-Table Output
    for i in range(len(r_list)):
            if 'EVPN' in valuelist[i][3][1]:
                    if "2:" in keylist[i]:
                            print  "Type 2 EVPN ---> Routes: {}".format(keylist[i])+" Protoco: {}".format(valuelist[i][3][1])
                    elif "3:" in keylist[i]:
                            print  "Type 3 EVPN ---> Routes: {}".format(keylist[i])+" Protoco: {}".format(valuelist[i][3][1])

    print "\n"

'''
sample output 
#-------Evpn Route Information for Device 192.168.0.83


Type 2 EVPN ---> Routes: 2:192.168.1.3:1::100::00:0c:29:4b:e9:00 Protoco: EVPN
Type 2 EVPN ---> Routes: 2:192.168.1.3:1::100::00:0c:29:4b:e9:0a Protoco: EVPN
Type 3 EVPN ---> Routes: 3:192.168.1.3:1::100::192.168.1.3 Protoco: EVPN


#-------Evpn Route Information for Device 192.168.0.84


Type 2 EVPN ---> Routes: 2:192.168.1.4:1::100::00:0c:29:4b:e9:14 Protoco: EVPN
Type 3 EVPN ---> Routes: 3:192.168.1.4:1::100::192.168.1.4 Protoco: EVPN

'''
