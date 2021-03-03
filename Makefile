#Makefile at top of application tree
TOP = .
ifdef EPICS_HOST_ARCH

include $(TOP)/configure/CONFIG
DIRS := $(DIRS) $(filter-out $(DIRS), configure)
#DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard *App))
#DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard *app))
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard iocBoot))
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard iocboot))
DIRS += digitelMpcApp

## Uncomment the following to build the simulation and example apps 
## (NB make sure configure/RELEASE is updated too)
#DIRS += exampleApp
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard etc))
# Comment out the following line to disable building of example iocs
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard iocs))


include $(TOP)/configure/RULES_TOP

clean:
	rm -rf $(TOP)/data
	
else

include $(TOP)/config/CONFIG_APP
#DIRS += config
#DIRS += $(wildcard *App)
#DIRS += $(wildcard *app)
#DIRS += $(wildcard iocBoot)
#DIRS += $(wildcard iocboot)
include $(TOP)/config/RULES_TOP


endif
