# coding=utf-8
#!/usr/bin/env python

from scapy.all import *

srcmac = '00:00:de:ad:be:ef'
dstmac = 'ff:ff:ff:ff:ff:ff'
bssid = '00:11:22:33:44:55'

# short preamble, not wpa/wep, short timeslot
beacon = Dot11Beacon(cap=0x2104)
ssid   = Dot11Elt(ID="SSID",info="MikeHasASmallAntena")
rates  = Dot11Elt(ID="Rates",info="\x82\x84\x8b\x96\x24\x30\x48\x6c")
dsset  = Dot11Elt(ID="DSset",info="\x03")
tim    = Dot11Elt(ID="TIM",info="\x00\x01\x00\x00") #no buffered traffic

pkt = RadioTap()/Dot11(type=0,subtype=8,addr1=dstmac)