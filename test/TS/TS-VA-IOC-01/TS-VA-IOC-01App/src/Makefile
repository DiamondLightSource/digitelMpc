TOP=../..

include $(TOP)/configure/CONFIG

USR_CXXFLAGS_DEFAULT += -fno-operator-names
USR_CXXFLAGS_DEFAULT += -pedantic

PROD_IOC = TS-VA-IOC-01

# TS-VA-IOC-01.dbd will be installed into <top>/dbd
DBD += TS-VA-IOC-01.dbd

# TS-VA-IOC-01.dbd will be created from these files
TS-VA-IOC-01_DBD += base.dbd
TS-VA-IOC-01_DBD += drvAsynIPPort.dbd
TS-VA-IOC-01_DBD += drvAsynSerialPort.dbd
TS-VA-IOC-01_DBD += stream.dbd
TS-VA-IOC-01_DBD += asynRecord.dbd

# TS-VA-IOC-01_registerRecordDeviceDriver.cpp will be created
# TS-VA-IOC-01.dbd
TS-VA-IOC-01_SRCS += TS-VA-IOC-01_registerRecordDeviceDriver.cpp

# These two lines are needed for non-vxWorks builds, such as Linux
TS-VA-IOC-01_SRCS_DEFAULT += TS-VA-IOC-01Main.cpp
TS-VA-IOC-01_SRCS_vxWorks += -nil-

# Add locally compiled object code
#TS-VA-IOC-01_SRCS +=

# The following adds object code from base/src/vxWorks
TS-VA-IOC-01_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# This line says that this IOC Application depends on the
# xxx Support Module
#TS-VA-IOC-01_LIBS += xxx
TS-VA-IOC-01_LIBS += asyn
#TS-VA-IOC-01_LIBS += pv
TS-VA-IOC-01_LIBS += stream
TS-VA-IOC-01_LIBS += pcre

# We need to link this IOC Application against the EPICS Base libraries
TS-VA-IOC-01_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
