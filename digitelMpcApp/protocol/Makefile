TOP = ../..
ifdef EPICS_HOST_ARCH
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

# Copy all protocol files into data directory


default:
	cp digitelMpc.proto $(TOP)/data
	dls-python generateMpcqProto.py


include $(TOP)/configure/RULES
endif
