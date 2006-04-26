TOP=../..

ifdef EPICS_HOST_ARCH

#=============================
# Build 3.14 stuff

include $(TOP)/configure/CONFIG

USR_CFLAGS += -DEPICS_R3_14



#=============================
# build an ioc example application

PROD_IOC_vxWorks = example
# example.dbd will be created and installed
DBD += example.dbd

# example.dbd will be made up from these files:
example_DBD += base.dbd
#example_DBD += stream.dbd
#example_DBD += sCalcoutRecord.dbd
example_DBD += calcSupport.dbd
example_DBD += drvAsynSerialPort.dbd
example_DBD += drvAsynIPPort.dbd
example_DBD += drvIpac.dbd
example_DBD += Hy8515.dbd
example_DBD += utility.dbd
example_DBD += ipSupport.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
example_SRCS += example_registerRecordDeviceDriver.cpp
example_SRCS_DEFAULT += exampleMain.cpp
example_SRCS_vxWorks += -nil-

# load libs xxxLibrary.o for vxWorks
#example_OBJS_vxWorks += $(STREAM)/bin/$(T_A)/streamLibrary
      
# The following adds support from base/src/vxWorks
example_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

example_LIBS += calc
example_LIBS += sscan
example_LIBS += ip
example_LIBS += asyn
#example_LIBS += stream
example_LIBS += drvHy8515
example_LIBS += Ipac
example_LIBS += utility
example_LIBS += seq pv
example_LIBS += $(EPICS_BASE_IOC_LIBS)


#=============================
# build an ioc simulation application

PROD_IOC = simulation
# simulation.dbd will be created and installed
DBD += simulation.dbd

# simulation.dbd will be made up from these files:
simulation_DBD += base.dbd
#simulation_DBD += stream.dbd
#simulation_DBD += drvAsynSerialPort.dbd
#simulation_DBD += drvAsynIPPort.dbd
simulation_DBD += pressArr.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
simulation_SRCS += simulation_registerRecordDeviceDriver.cpp
simulation_SRCS_DEFAULT += simulationMain.cpp
simulation_SRCS_vxWorks += -nil-

# load libs xxxLibrary.o for vxWorks
#simulation_OBJS_vxWorks += $(STREAM)/bin/$(T_A)/streamLibrary
      
# The following adds support from base/src/vxWorks
simulation_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

simulation_LIBS += asyn
#simulation_LIBS += stream
simulation_LIBS += pressArr
simulation_LIBS += $(EPICS_BASE_IOC_LIBS)



include $(TOP)/configure/RULES

else

#===========================
#Build 3.13 stuff

include $(TOP)/config/CONFIG_APP
include $(TOP)/config/RULES_ARCHS

endif


#===========================
