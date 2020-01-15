TOP=../..

# The following switch is required if compiling C++
# # gensub modules, as the genSubRecord structure declares
# # a member 'unsigned long	not;'
# # However, 'not' has been made a non-ansi reserved word
# # but can be switch off as such by this compiler switch :)
USR_CXXFLAGS_DEFAULT += -fno-operator-names
USR_CXXFLAGS_DEFAULT += -pedantic

include $(TOP)/configure/CONFIG

LIBRARY_IOC = digitelMpc

# digitelMpc.dbd will be created from these files
DBD += digitelMpc.dbd
digitelMpc_DBD += base.dbd
digitelMpc_DBD += calcSupport.dbd
digitelMpc_DBD += digitelMpcSupport.dbd

# digitelMpc_registerRecordDeviceDriver.cpp will be created
# digitelMpc.dbd
digitelMpc_SRCS += digitelMpc_registerRecordDeviceDriver.cpp
digitelMpc_SRCS += model.c

digitelMpc_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES

