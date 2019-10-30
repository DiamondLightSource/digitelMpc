TOP=../..

include $(TOP)/configure/CONFIG

LIBRARY_IOC = digitelMpc

# digitelMpc.dbd will be installed into <top>/dbd
DBD += digitelMpc.dbd

# digitelMpc.dbd will be created from these files
DBD += digitelMpc.dbd
digitelMpc_DBD += base.dbd
digitelMpc_DBD += calcSupport.dbd

# digitelMpc_registerRecordDeviceDriver.cpp will be created
# digitelMpc.dbd
digitelMpc_SRCS += digitelMpc_registerRecordDeviceDriver.cpp

digitelMpc_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES

