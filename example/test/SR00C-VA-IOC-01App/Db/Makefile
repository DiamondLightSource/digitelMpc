TOP=../..
include $(TOP)/configure/CONFIG
DB += SR00C-VA-IOC-01.db

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

# SR00C_DBD += drvAsynIPPort.dbd
# SR00C_DBD += drvAsynSerialPort.dbd

SR00C: ../O.Common/SR00C-VA-IOC-01.db
	/dls_sw/prod/tools/RHEL6-x86_64/defaults/bin/epicsparser.py ../O.Common/SR00C-VA-IOC-01.db -r SR00C -s as > SR00C
	@echo "Installing postprocessor files:... INSTALL_PRODUCT=$(INSTALL_PRODUCT) - INSTALL_DATA=$(INSTALL_DATA)"
	-@$(INSTALL_PRODUCT) -d -m 555 *.req $(INSTALL_DATA)

buildInstall: SR00C

