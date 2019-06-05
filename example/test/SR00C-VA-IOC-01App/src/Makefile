TOP=../..

include $(TOP)/configure/CONFIG

# ------------------------
# Build an IOC Application
# ------------------------

PROD_IOC = SR00C-VA-IOC-01

# SR00C-VA-IOC-01.dbd will be installed into <top>/dbd
DBD += SR00C-VA-IOC-01.dbd

# SR00C-VA-IOC-01.dbd will be created from these files
SR00C-VA-IOC-01_DBD += base.dbd
SR00C-VA-IOC-01_DBD += drvAsynSerialPort.dbd
SR00C-VA-IOC-01_DBD += stream.dbd
SR00C-VA-IOC-01_DBD += calcSupport.dbd

SR00C-VA-IOC-01_SRCS += SR00C-VA-IOC-01_registerRecordDeviceDriver.cpp

SR00C-VA-IOC-01_SRCS_DEFAULT += SR00C-VA-IOC-01Main.cpp

# Add locally compiled object code
#SR00C-VA-IOC-01_SRCS +=

# This line says that this IOC Application depends on the
# xxx Support Module
SR00C-VA-IOC-01_LIBS += stream
SR00C-VA-IOC-01_LIBS += asyn
SR00C-VA-IOC-01_LIBS += calc

# We need to link this IOC Application against the EPICS Base libraries
SR00C-VA-IOC-01_LIBS += $(EPICS_BASE_IOC_LIBS)


include $(TOP)/configure/RULES
