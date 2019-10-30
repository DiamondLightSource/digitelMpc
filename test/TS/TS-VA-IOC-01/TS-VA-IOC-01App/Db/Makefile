TOP=../..
include $(TOP)/configure/CONFIG

DB += TS-VA-IOC-01.db


include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

TS: ../O.Common/TS-VA-IOC-01.db
	/dls_sw/prod/tools/RHEL6-x86_64/defaults/bin/epicsparser.py ../O.Common/TS-VA-IOC-01.db -r TS -s as > TS
	@echo "Installing postprocessor files:... INSTALL_PRODUCT=$(INSTALL_PRODUCT) - INSTALL_DATA=$(INSTALL_DATA)"
	-@$(INSTALL_PRODUCT) -d -m 555 *.req $(INSTALL_DATA)

buildInstall: TS
