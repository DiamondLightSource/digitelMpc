###########################################################
# Pete Owens 6/2/04 vxWorks/EPICS startup file, 
# Example to test simulated digitelMpc ornlSerial application
#

#digitelMpcTop = "/home/pho/diamond/digitelMpc_ornlSerial"
digitelMpcTop = "/home/diamond/R3.13.9/work/support/digitelMpc_ornlSerial/Rx-y"
diamondTop = "/home/diamond/R3.13.9/work/support/superTop/Rx-y"

###########################################################

cd diamondTop
cd "bin/ppc604" 
ld < iocCore
ld < baseLib  
ld < pressArrLib

###########################################################

cd diamondTop
cd "dbd"
dbLoadDatabase "baseApp.dbd"

###########################################################

cd digitelMpcTop
cd "example"

dbLoadTemplate ("simulation_digitelMpc.substitutions")

iocInit

###########################################################
