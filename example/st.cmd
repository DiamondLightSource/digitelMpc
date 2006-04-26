###########################################################
# Pete Owens 23/9/03 vxWorks/EPICS startup file, 
# Example to test tart ornlSerial with digitelMpc extension
# This IOC is configured for :
#       Hytec IP Carrier 8002 card in slot 8 - 
#       Greenspring IPOctal serial module in slot B
#	Digitel MPC units on ports 4 & 5
#

#digitelMpcTop = "/home/pho/diamond/digitelMpc_ornlSerial"
digitelMpcTop = "/home/diamond/R3.13.9/work/support/digitelMpc_ornlSerial/Rx-y"
diamondTop = "/home/diamond/R3.13.9/work/support/superTop/Rx-y"

###########################################################
# Configure serial port number here
#  
IPSLOTA = 0
IPSLOTB = 1
IPSLOTC = 2
IPSLOTD = 3

VMESLOT = 7
IPSLOT  = IPSLOTB
PORTNUM = 4
CARDNUM = (10 * VMESLOT) + IPSLOT
###########################################################

cd diamondTop
cd "bin/ppc604" 
ld < iocCore
ld < seq
ld < baseLib  
ld < utilityLib
ld < ornlSerialLib 
ld < ipacLib
ld < tyGSOctal.o
ld < drvHy8515.o

cd digitelMpcTop 
ld < bin/ppc604/digitelMpc.o

#############################################

cd diamondTop
cd "dbd"
dbLoadDatabase "baseApp.dbd"
dbLoadDatabase "drvIpac.dbd" 
dbLoadDatabase "ornlSerial.dbd" 

###########################################################
# Configure a  Hytec 8002 IP carrier card 
#
ARGS = malloc (20)
IVEC = newInterruptVector ()
sprintf (ARGS, "%d %d %d", VMESLOT, 2, IVEC)
CARRIER = ipacEXTAddCarrier (&EXTHy8002, ARGS)


###########################################################
# Configure Hytec 8515 IPOctal serial module  
#
# Params are : 
#	cardnum, 
#	vmeslotnum, 
#	ipslotnum, 
#	vectornum, 
#	intdelay (-ve => FIFO interrupt), 
#	halfduplexmode, 
#	delay845
#
IVEC   = newInterruptVector ()
MODNUM = Hy8515Configure (CARDNUM, CARRIER, IPSLOT, IVEC, -32, 0, 0)

# Create device
# Params are :
#	name
#	card number
#	port number
#	read buffer size
#	write buffer size
#
MPCPORT = tyHYOctalDevCreate ("/ty/mpc/0", MODNUM, PORTNUM, 2500, 250)
tyHYOctalConfig (MPCPORT, 9600, 'N', 1, 8, 'N')

###########################################################

cd digitelMpcTop
cd "example"

devMgrInit ("ioc.devices")
dbLoadTemplate ("digitelMpc.substitutions")

###########################################################
# switch on debugging
#digitelMpcDebug=1

iocInit

###########################################################
